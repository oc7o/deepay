from typing import Any, Optional

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.views.generic import DetailView, ListView

from deepay.apps.basket.models import Basket
from deepay.apps.inventory.forms import AddToBasketForm
from deepay.apps.inventory.models import Product, ProductInventory


class ProductInventoryDetailView(DetailView):
    model = ProductInventory
    template_name = "inventory/product-inventory-detail.html"
    context_object_name = "inventory"

    # TODO: post -> add to basket

    def post(self, request, *args, **kwargs):
        form = AddToBasketForm(request.POST)
        if form.is_valid():
            qty = form.cleaned_data["qty"]
            inventory = self.get_object()
            basket = Basket.objects.get(web_id=request.session.get("basket_web_id"))

            inventory.add_to_basket(
                basket,
                qty,
            )
        return self.get(request, *args, **kwargs)

    def get_object(self):
        qs = self.get_queryset().get(web_id=self.kwargs["web_id"])
        return qs


class MyProductsView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "inventory/my-products.html"
    context_object_name = "products"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class ProductInventoriesView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "inventory/product-inventories.html"
    context_object_name = "product"

    # def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
    def get_object(self):
        qs = self.get_queryset().get(web_id=self.kwargs["web_id"])
        return qs
        # return super().get_object(queryset)

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     return qs.filter(product=self.request.user)
