"""
Users Admin
"""

# Django
from django.contrib import admin

#Models
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_superuser', 'is_staff']
