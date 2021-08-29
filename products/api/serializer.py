"""
Products Serializers
"""

# Django RestFramework
from rest_framework import serializers

# Models
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"