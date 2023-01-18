from django.contrib import admin

from .models import BTCPayClientStore, Order, OrderProductInventory

admin.site.register(BTCPayClientStore)
admin.site.register(Order)
admin.site.register(OrderProductInventory)
