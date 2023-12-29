from django.views.generic import DetailView, TemplateView

from deepay.apps.basket.models import Basket, BasketObject


class BasketView(TemplateView):
    template_name = "basket/basket.html"

    def post(self, request, *args, **kwargs):
        if "delete" in request.POST:
            basket_object = BasketObject.objects.get(web_id=request.POST["delete"])
            basket_object.delete()

        return self.get(request, *args, **kwargs)


class CreateOrderView(TemplateView):
    template_name = "basket/create_order.html"
