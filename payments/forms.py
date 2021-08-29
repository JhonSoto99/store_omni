"""
Payments forms.
"""

# Django
from django import forms

# Models
from .models import *
from orders.models import Order


class PaymentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(PaymentForm, self).__init__(*args, **kwargs)
        self.fields['orders'] = forms.ModelMultipleChoiceField(
            queryset=Order.objects.filter(
                created_by=user,
                paid_out=False
            )
        )

    class Meta:
        model = Payment
        fields = [
            'orders'
        ]