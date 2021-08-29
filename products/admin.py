"""
Product Admin
"""

# Django
from django.contrib import admin

#Models
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'name', 'description', 'price', 'enabled']


