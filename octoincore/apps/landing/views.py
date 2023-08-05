from django.shortcuts import render
from django.views.generic import TemplateView

from octoincore.apps.inventory.models import Product


class LandingView(TemplateView):
    template_name = "landing/landing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()

        print(
            1, Product.objects.first().inventories.first().media_files.first().image.url
        )
        return context
