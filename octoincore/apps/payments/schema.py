import datetime
import typing
from decimal import Decimal

import strawberry
from django.conf import settings

from octoincore.apps.basket.models import Basket
from octoincore.apps.captcha.models import Captcha
from octoincore.apps.inventory.models import ProductInventory
from octoincore.apps.inventory.schema import ProductInventoryType
from octoincore.permission import IsAuthenticated
from octoincore.types import JSON  # from strawberry.scalars import JSON

from .btcpayserver_client import get_btcpay_client
from .models import Order, OrderInvoice

if typing.TYPE_CHECKING:
    from octoincore.apps.basket.schema import BasketType


@strawberry.django.type(model=OrderInvoice)
class OrderInvoiceType:
    invoice_id: str
    invoice_url: str
    price: float
    created_at: datetime.datetime
    expired_at: datetime.datetime


@strawberry.django.type(model=Order)
class OrderType:
    firstname: str
    lastname: str
    email: str
    street: str
    city: str
    zip_code: str
    status: str
    created_at: datetime.datetime | None
    web_id: str

    basket: typing.Annotated[
        "BasketType", strawberry.lazy("octoincore.apps.basket.schema")
    ]
    invoice: OrderInvoiceType | None

    @strawberry.field
    def total_price(self, info) -> Decimal:
        # This is not like basket.total_price() because we want to get the price for the vendor
        total_price = 0
        for basket_object in self.basket.basket_objects.all():
            if (
                basket_object.product_inventory.product.owner
                == info.context.request.user
            ):
                total_price += (
                    basket_object.product_inventory.store_price * basket_object.quantity
                )
        return total_price


@strawberry.type
class PaymentsQuery:
    @strawberry.field
    def invoices(self, info) -> typing.List[JSON]:
        return get_btcpay_client().get_invoices()

    @strawberry.field
    def check_order(self, info, web_id: str) -> OrderType:
        return Order.objects.get(web_id=web_id)

    @strawberry.field(permission_classes=[IsAuthenticated])
    def my_orders(self, info) -> typing.List[OrderType]:
        orders = Order.objects.filter(
            basket__basket_objects__product_inventory__product__owner=info.context.request.user
        )
        return orders


@strawberry.type
class PaymentsMutation:
    @strawberry.mutation
    def create_order(
        self,
        info,
        basket_web_id: str,
        firstname: str,
        lastname: str,
        city: str,
        street: str,
        zip_code: str,
        email: str,
        captcha_web_id: str,
        captcha_text: str,
    ) -> OrderType:
        captcha = Captcha.objects.get(web_id=captcha_web_id)
        if captcha.text != captcha_text:
            captcha.delete()
            raise Exception("Captcha is not valid")
        captcha.delete()

        basket = Basket.objects.get(web_id=basket_web_id)

        if hasattr(basket, "order"):
            raise Exception("Basket is already ordered")

        out_of_stock = []
        for basket_object in basket.basket_objects.all():
            if basket_object.quantity > basket_object.product_inventory.stock.units:
                out_of_stock.append(
                    {
                        "product": basket_object.product_inventory.product.name,
                        "quantity": basket_object.quantity,
                        "stock": basket_object.product_inventory.stock.units,
                    }
                )

        if len(out_of_stock) > 0:
            raise Exception("Out of stock", out_of_stock)

        order = Order()
        order.firstname = firstname
        order.lastname = lastname
        order.city = city
        order.street = street
        order.zip_code = zip_code
        order.email = email
        order.basket = basket
        order.save()

        basket.locked = True
        basket.save()

        order_invoice = get_btcpay_client().create_invoice(
            amount=float(basket.total_price)
        )
        print("order_invoice", order_invoice)

        invoice = OrderInvoice()
        invoice.order = order
        invoice.invoice_id = order_invoice["id"]
        invoice.invoice_url = order_invoice["checkoutLink"]
        invoice.price = order_invoice["amount"]
        invoice.save()

        print("invoice", invoice)

        return order
