"""
Payments Serializers
"""

# Django RestFramework
from rest_framework import serializers

# Models
from payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"