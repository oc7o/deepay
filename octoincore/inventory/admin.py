from .models import (
    Brand,
    Category,
    Media,
    Product,
    ProductAttribute,
    ProductAttributeValue,
    ProductAttributeValues,
    ProductInventory,
    ProductType,
    Stock,
)
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Product)
admin.site.register(ProductAttribute)
admin.site.register(ProductType)
admin.site.register(Brand)
admin.site.register(Media)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductInventory)
admin.site.register(Stock)
admin.site.register(ProductAttributeValues)
