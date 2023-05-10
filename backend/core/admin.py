from django.contrib import admin
from .models import (
    Attribute, AttributeName, AttributeValue, Catalog, Image,
    Product, ProductAttributes, ProductImage
)

admin.site.register(Attribute)
admin.site.register(AttributeName)
admin.site.register(AttributeValue)
admin.site.register(Catalog)
admin.site.register(Image)
admin.site.register(Product)
admin.site.register(ProductAttributes)
admin.site.register(ProductImage)
