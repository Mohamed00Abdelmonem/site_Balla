from django.contrib import admin
from .models import Product, CartItem, Cart

# Register your models here.

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Product)