"""
Orders test model.
"""

# Django
from django.db.utils import IntegrityError
from django.test import TestCase

# Model
from .models import Order, OrderProducts
from accounts.models import User
from products.models import Product


class OrderTestCase(TestCase):

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

    def test_create_order(self):
        user = User.objects.create(**self.user)
        order = Order.objects.create(created_by=user)
        self.assertIsNotNone(order.uuid)

    def test_add_product_to_order(self):
        user = User.objects.create(**self.user)
        order = Order.objects.create(created_by=user)
        product = Product.objects.create(**self.product)
        product_order = OrderProducts.objects.create(order=order, product=product)
        self.assertIsNotNone(product_order.uuid)

    def test_update_amount_order(self):
        user = User.objects.create(**self.user)
        order = Order.objects.create(created_by=user)
        product = Product.objects.create(**self.product)
        OrderProducts.objects.create(order=order, product=product)

        order_updated_amount = Order.objects.get(uuid=order.uuid)
        self.assertNotEqual(order_updated_amount.amount, 0)




