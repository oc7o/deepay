from django.urls import path

from deepay.apps.vendor.views import OrderedBasketObjectsView

app_name = "vendor"

urlpatterns = [
    path("orders/", OrderedBasketObjectsView.as_view(), name="ordered-basket-objects"),
]
