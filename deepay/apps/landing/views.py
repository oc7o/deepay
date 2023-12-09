from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from deepay.apps.inventory.models import Product


class LandingView(ListView):
    template_name = "landing/landing.html"
    context_object_name = "products"
    model = Product

    paginate_by = 8
