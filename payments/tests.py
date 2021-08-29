"""
Payments test model.
"""

# Django
from django.db.utils import IntegrityError
from django.test import TestCase

# Model
from .models import Payment
from orders.models import Order, OrderProducts
from accounts.models import User
from products.models import Product


class PaymentTestCase(TestCase):

    def setUp(self):
        self.user = {
            'email': 'jhon@gmail.com',
            'password': 'AS355GG675',
            'first_name': 'Jhon',
            'last_name': 'Soto'
        }

    def test_create_payments(self):
        user = User.objects.create(**self.user)
        order = Order.objects.create(created_by=user)
        payment = Payment.objects.create(amount=50000, created_by=user)
        payment.orders.add(order.uuid)
        self.assertIsNotNone(payment.uuid)






