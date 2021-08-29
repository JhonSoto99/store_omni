"""
Order forms.
"""

# Django
from django import forms

# Models
from .models import *


class OrderProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(OrderProductForm, self).__init__(*args, **kwargs)
        self.fields['order'] = forms.ModelChoiceField(
            queryset=Order.objects.filter(
                created_by=user,
                paid_out=False,
                sent=False,
            )
        )

    class Meta:
        model = OrderProducts
        fields = [
            'order'
        ]