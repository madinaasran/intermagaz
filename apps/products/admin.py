from django.contrib import admin
from apps.products.models import Product, Like

admin.site.register(Product)
admin.site.register(Like)