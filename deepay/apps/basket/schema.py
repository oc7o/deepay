import typing
import uuid
from datetime import datetime
from decimal import Decimal

import strawberry

from deepay.apps.inventory.models import ProductInventory
from deepay.apps.inventory.schema import ProductInventoryType

from .models import Basket, BasketObject

if typing.TYPE_CHECKING:
    from deepay.apps.payments.schema import OrderType


@strawberry.django.type(model=BasketObject)
class BasketObjectType:
    web_id: str
    inventory: typing.Annotated["ProductInventoryType", "ProductInventoryType"]
    qty: int
    created_at: datetime
    updated_at: datetime


@strawberry.django.type(model=Basket)
class BasketType:
    web_id: str
    created_at: datetime
    updated_at: datetime
    basket_objects: typing.List[
        typing.Annotated["BasketObjectType", "BasketObjectType"]
    ]
    total_price: Decimal
    total_qty: int
    order: typing.Annotated[
        "OrderType", strawberry.lazy("deepay.apps.payments.schema")
    ] | None

    @strawberry.field
    def vendor_basket_objects(self, info) -> typing.List[BasketObjectType]:
        return (
            BasketObject.objects.filter(basket=self)
            .filter(
                inventory__product__owner=info.context.request.user,
            )
            .all()
        )


@strawberry.type
class BasketQuery:
    @strawberry.field
    def basket(self, info, web_id: str) -> BasketType:
        basket = Basket.objects.get(web_id=web_id)
        order = basket.order if hasattr(basket, "order") else None
        return BasketType(
            web_id=basket.web_id,
            created_at=basket.created_at,
            updated_at=basket.updated_at,
            basket_objects=basket.basket_objects.all(),
            total_price=basket.total_price,
            total_qty=basket.total_qty,
            order=order,
            vendor_basket_objects=basket.vendor_basket_objects(info),
        )


@strawberry.type
class BasketMutation:
    @strawberry.mutation
    def create_basket(self, info) -> BasketType:
        basket = Basket.objects.create()
        return basket

    @strawberry.mutation
    def add_to_basket(
        self, info, basket_web_id: str, inventory_web_id: str, qty: int
    ) -> BasketType:
        basket = Basket.objects.get(web_id=basket_web_id)
        if basket.locked:
            raise Exception("Basket is locked")
        inventory = ProductInventory.objects.get(web_id=inventory_web_id)
        basket_objects = BasketObject.objects.filter(basket=basket, inventory=inventory)
        if basket_objects.exists():
            basket_object = basket_objects.first()
            basket_object.qty += qty
            basket_object.save()
        else:
            basket_object = BasketObject.objects.create(
                basket=basket,
                inventory=inventory,
                qty=qty,
            )
        return basket

    @strawberry.mutation
    def remove_from_basket(
        self, info, basket_web_id: str, inventory_web_id: str
    ) -> BasketType:
        basket = Basket.objects.get(web_id=basket_web_id)
        if basket.locked:
            raise Exception("Basket is locked")
        inventory = ProductInventory.objects.get(web_id=inventory_web_id)
        basket_object = BasketObject.objects.get(
            basket=basket,
            inventory=inventory,
        )
        basket_object.delete()
        return basket

    @strawberry.mutation
    def update_basket(
        self, info, basket_web_id: str, inventory_web_id: str, qty: int
    ) -> BasketType:
        basket = Basket.objects.get(web_id=basket_web_id)
        if basket.locked:
            raise Exception("Basket is locked")
        inventory = ProductInventory.objects.get(web_id=inventory_web_id)
        basket_object = BasketObject.objects.get(
            basket=basket,
            inventory=inventory,
        )
        basket_object.qty = qty
        basket_object.save()
        return basket

    @strawberry.mutation
    def empty_basket(self, info, basket_web_id: str) -> BasketType:
        basket = Basket.objects.get(web_id=basket_web_id)
        if basket.locked:
            raise Exception("Basket is locked")
        basket.basket_objects.all().delete()
        return basket

    @strawberry.mutation
    def delete_basket(self, info, web_id: str) -> BasketType:
        basket = Basket.objects.get(web_id=web_id)
        if basket.locked:
            raise Exception("Basket is locked")
        basket.delete()
        return basket
