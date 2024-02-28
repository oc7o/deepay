from django.shortcuts import render
from django.views.generic import TemplateView
from deepay.apps.inventory.models import ProductInventory
from deepay.apps.basket.models import BasketObject


class OrderedBasketObjectsView(TemplateView):
    template_name = "vendor/ordered_basket_objects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["basket_objects"] = BasketObject.objects.filter(
            inventory__product__owner=self.request.user,
            basket__isnull=False,
        )
        return context
