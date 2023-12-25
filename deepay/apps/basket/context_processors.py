import json
from uuid import UUID

from .models import Basket


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)


def basket_context(request):
    basket_web_id = request.session.get("basket_web_id", None)
    if basket_web_id is None:
        basket = Basket.objects.create()
        request.session["basket_web_id"] = str(basket.web_id)
    else:
        basket = Basket.objects.get(web_id=basket_web_id)

    return {
        "basket": basket,
    }
