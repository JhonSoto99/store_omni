"""
Product forms.
"""

# Django
from django import forms

# Models
from .models import *


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'