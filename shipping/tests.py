"""
Shipping test model.
"""

# Django
from django.db.utils import IntegrityError
from django.test import TestCase

# Model
from .models import Shipping
from accounts.models import User
from orders.models import Order


class ShippingTestCase(TestCase):

    def setUp(self):
        self.user = {
            'email': 'jhon@gmail.com',
            'password': 'AS355GG675',
            'first_name': 'Jhon',
            'last_name': 'Soto'
        }

        self.product = {
            'name': 'MacBooc Pro',
            'description': '1tb ssd',
            'price': 3000000,
            'enabled': True
        }

    def test_create_shipping(self):
        user = User.objects.create(**self.user)
        order = Order.objects.create(created_by=user)
        shipping = Shipping.objects.create(created_by=user, received=True)
        shipping.orders.add(order)
        self.assertIsNotNone(shipping.uuid)




