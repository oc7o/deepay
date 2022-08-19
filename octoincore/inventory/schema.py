import typing

import strawberry

from .models import (
    Brand,
    Category,
    Media,
    Product,
    ProductAttribute,
    ProductAttributeValues,
    ProductInventory,
    ProductType,
    Stock,
)


@strawberry.django.type(model=Product)
class ProdctType:
    web_id: str
    slug: str
    name: str
    description: str
    # category: 
    is_active: bool
    created_at: str
    updated_at: str


# def resolve_products():
#     return Product.objects.all()

@strawberry.type
class InventoryQuery:
    # products: typing.List[ProductType] = strawberry.django.field()

    @strawberry.field
    def products(self, info: strawberry.types.Info) -> typing.List[ProdctType]:
        return Product.objects.all()
