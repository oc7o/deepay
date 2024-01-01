from django.urls import path

from deepay.apps.inventory.views import (
    MyProductsView,
    ProductInventoriesView,
    ProductInventoryDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductInventoryCreateView,
    AddMediaView,
    ProductInventoryUpdateView,
    ProductInventoryDeleteView,
)

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
    path(
        "my-products/<uuid:web_id>/create-inventory/",
        ProductInventoryCreateView.as_view(),
        name="inventory-create",
    ),
    path(
        "my-inventories/<uuid:web_id>/add-media/",
        AddMediaView.as_view(),
        name="inventory-add-media",
    ),
    path(
        "my-inventories/<uuid:web_id>/edit/",
        ProductInventoryUpdateView.as_view(),
        name="inventory-update",
    ),
    path(
        "my-inventories/<uuid:web_id>/delete/",
        ProductInventoryDeleteView.as_view(),
        name="inventory-delete",
    ),
    path(
        "my-products/<uuid:web_id>/edit/",
        ProductUpdateView.as_view(),
        name="product-update",
    ),
    path(
        "my-products/<uuid:web_id>/delete/",
        ProductDeleteView.as_view(),
        name="product-delete",
    ),
    path(
        "p/<uuid:web_id>/",
        ProductInventoryDetailView.as_view(),
        name="product-inventory-detail",
    ),
    path(
        "create-product/",
        ProductCreateView.as_view(),
        name="product-create",
    ),
]
