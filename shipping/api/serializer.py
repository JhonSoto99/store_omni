"""
SHIPPING Serializers
"""

# Django RestFramework
from rest_framework import serializers

# Models
from shipping.models import Shipping


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = "__all__"