"""
Payments forms.
"""

# Django
from django import forms

# Models
from .models import *
from orders.models import Order


class ShippingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ShippingForm, self).__init__(*args, **kwargs)
        self.fields['orders'] = forms.ModelMultipleChoiceField(
            queryset=Order.objects.filter(
                sent=False,
                paid_out=True
            )
        )

    class Meta:
        model = Shipping
        fields = [
            'orders'
        ]