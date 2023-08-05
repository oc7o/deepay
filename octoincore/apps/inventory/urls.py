from django.urls import path

from octoincore.apps.inventory.views import MyProductsView, ProductInventoriesView

app_name = "inventory"

urlpatterns = [
    path("my-products/", MyProductsView.as_view(), name="my-products"),
    # path("create-product/", MyProductsView.as_view(), name="my-products"),
    # path("my-products/<web_id:slug>", MyProductsView.as_view(), name="my-products"),
    path(
        "my-products/<uuid:web_id>/inventories/",
        ProductInventoriesView.as_view(),
        name="product-inventories",
    ),
]
