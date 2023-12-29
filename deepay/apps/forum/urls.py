from django.urls import path

from deepay.apps.forum.views import (
    ThreadCreateView,
    ThreadListView,
    ThreadPostsView,
    PostCreateView,
    PostDetailView,
    ThreadDeleteView,
)

app_name = "forum"

urlpatterns = [
    path("threads/", ThreadListView.as_view(), name="thread-list"),
    path("t/<slug:slug>/delete/", ThreadDeleteView.as_view(), name="thread-delete"),
    path("t/<slug:slug>/", ThreadPostsView.as_view(), name="thread-detail"),
    path("create-thread/", ThreadCreateView.as_view(), name="thread-create"),
    path("t/<slug:slug>/create-post/", PostCreateView.as_view(), name="post-create"),
    path("p/<uuid:web_id>/", PostDetailView.as_view(), name="post-detail"),
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
