from django.urls import path

from deepay.apps.forum.views import ThreadCreateView, ThreadListView, ThreadPostsView

app_name = "forum"

urlpatterns = [
    path("threads/", ThreadListView.as_view(), name="thread-create"),
    path("s/<slug:slug>/", ThreadPostsView.as_view(), name="thread-detail"),
    path("create-thread/", ThreadCreateView.as_view(), name="thread-create")
    # path("create-product/", MyProductsView.as_view(), name="my-products"),
    # path("my-products/<web_id:slug>", MyProductsView.as_view(), name="my-products"),
    # path(
    #     "my-products/<uuid:web_id>/inventories/",
    #     ProductInventoriesView.as_view(),
    #     name="product-inventories",
    # ),
    # path(
    #     "p/<uuid:web_id>/",
    #     ProductInventoryDetailView.as_view(),
    #     name="product-inventory-detail",
    # ),
]
