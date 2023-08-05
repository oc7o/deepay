from django.views.generic import DetailView, TemplateView


class BasketView(TemplateView):
    template_name = "basket/basket.html"
