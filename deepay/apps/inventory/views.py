from typing import Any, Optional

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse

from deepay.apps.basket.models import Basket
from deepay.apps.inventory.forms import (
    AddToBasketForm,
    ProductInventoryCreateForm,
    ProductInventoryUpdateForm,
)
from deepay.apps.inventory.models import Product, ProductInventory, Stock, Media


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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ["name", "description", "category"]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.is_active = False
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "inventory:product-inventories", kwargs={"web_id": self.object.web_id}
        )


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ["name", "description", "category", "is_active"]

    def get_object(self):
        qs = self.get_queryset().get(web_id=self.kwargs["web_id"])
        return qs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.is_active = False
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "inventory:product-inventories", kwargs={"web_id": self.object.web_id}
        )


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product

    def get_object(self):
        qs = self.get_queryset().get(web_id=self.kwargs["web_id"])
        return qs

    def get_success_url(self):
        return reverse("inventory:my-products")


class ProductInventoriesView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "inventory/product-inventories.html"
    context_object_name = "product"

    # def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
    def get_object(self):
        qs = self.get_queryset().get(web_id=self.kwargs["web_id"])
        return qs


class ProductInventoryCreateView(LoginRequiredMixin, CreateView):
    model = ProductInventory
    form_class = ProductInventoryCreateForm

    def form_valid(self, form):
        form.instance.product = Product.objects.get(web_id=self.kwargs["web_id"])
        form.instance.is_active = False
        form.instance.stock = Stock.objects.create(units=self.request.POST.get("units"))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "inventory:product-inventories",
            kwargs={"web_id": self.object.product.web_id},
        )


class ProductInventoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductInventory
    form_class = ProductInventoryUpdateForm

    def get_object(self):
        qs = self.get_queryset().get(web_id=self.kwargs["web_id"])
        return qs

    def form_valid(self, form):
        form.instance.stock.units = self.request.POST.get("units")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "inventory:product-inventories",
            kwargs={"web_id": self.object.product.web_id},
        )


class ProductInventoryDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductInventory

    def get_object(self):
        qs = self.get_queryset().get(web_id=self.kwargs["web_id"])
        return qs

    def get_success_url(self):
        return reverse(
            "inventory:product-inventories",
            kwargs={"web_id": self.object.product.web_id},
        )


class AddMediaView(LoginRequiredMixin, CreateView):
    model = Media
    fields = ["image"]

    def form_valid(self, form):
        form.instance.inventory = ProductInventory.objects.get(
            web_id=self.kwargs["web_id"]
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "inventory:product-inventories",
            kwargs={"web_id": self.object.inventory.product.web_id},
        )
