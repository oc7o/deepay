from django.urls import path

from .views import BasketView, CreateOrderView, OrderSuccessView

app_name = "basket"

urlpatterns = [
    path("", BasketView.as_view(), name="basket"),
    path("create-order/", CreateOrderView.as_view(), name="create-order"),
    path("success/", OrderSuccessView.as_view(), name="success"),
]
