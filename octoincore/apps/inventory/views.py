from typing import Any, Optional

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.views.generic import DetailView, ListView

from octoincore.apps.inventory.models import Product, ProductInventory


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
