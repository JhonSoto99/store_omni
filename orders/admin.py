"""
Order Admin
"""

# Django
from django.contrib import admin

#Models
from .models import Order, OrderProducts


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'paid_out', 'sent', 'created_by']


@admin.register(OrderProducts)
class OrderProductsAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'product', 'order']



