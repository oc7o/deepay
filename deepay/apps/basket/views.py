from django.views.generic import DetailView, TemplateView

from deepay.apps.basket.models import Basket, BasketObject
from deepay.apps.payments.models import Order, OrderInvoice
from deepay.apps.payments.utils import get_btcpay_client

from django.shortcuts import redirect
from django.urls import reverse


class BasketView(TemplateView):
    template_name = "basket/basket.html"

    def post(self, request, *args, **kwargs):
        if "delete" in request.POST:
            basket_object = BasketObject.objects.get(web_id=request.POST["delete"])
            basket_object.delete()

        return self.get(request, *args, **kwargs)


class CreateOrderView(TemplateView):
    template_name = "basket/create_order.html"

    def post(self, request, *args, **kwargs):
        basket_web_id = request.session.get("basket_web_id", None)
        if not basket_web_id:
            return self.get(request, *args, **kwargs)  # TODO: error

        basket = Basket.objects.get(web_id=basket_web_id)

        print("basket.total_price", basket.total_price)

        # Check if basket is locked
        if basket.locked:
            raise Exception("Basket is locked")

        # Check if basket is already ordered
        if hasattr(basket, "order"):
            raise Exception("Basket is already ordered")

        # Check if basket is empty
        if basket.basket_objects.count() == 0:
            raise Exception("Basket is empty")

        # Check if basket is out of stock
        out_of_stock = []
        for basket_object in basket.basket_objects.all():
            if basket_object.qty > basket_object.inventory.stock.units:
                out_of_stock.append(
                    {
                        "product": basket_object.inventory.product.name,
                        "qty": basket_object.qty,
                        "stock": basket_object.inventory.stock.units,
                    }
                )

        if len(out_of_stock) > 0:
            raise Exception("Out of stock", out_of_stock)

        order = Order.objects.create(
            firstname=request.POST["firstname"],
            lastname=request.POST["lastname"],
            email=request.POST["email"],
            street=request.POST["street"],
            city=request.POST["city"],
            zip_code=request.POST["zip_code"],
            status="new",
            basket=basket,
        )

        basket.locked = True
        basket.save()

        order_invoice = get_btcpay_client().create_invoice(
            amount=float(basket.total_price),
            redirect_url=request.build_absolute_uri(reverse("basket:success")),
        )
        print("order_invoice", order_invoice)

        invoice = OrderInvoice.objects.create(
            order=order,
            invoice_id=order_invoice["id"],
            invoice_url=order_invoice["checkoutLink"],
            price=order_invoice["amount"],
        )

        print("invoice", invoice)

        print("DONE!")

        return redirect(invoice.invoice_url)


class OrderSuccessView(TemplateView):
    template_name = "basket/success.html"
