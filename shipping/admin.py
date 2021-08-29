"""
Shipping Admin
"""

# Django
from django.contrib import admin

#Models
from .models import Shipping


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ['uuid']