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

class ProductsViewTestCase(TestCase):
    """
    Test Views Orders
    """

    def setUp(self):
        self.jhon = {
            'username': 'jhon@gmail.com',
            'password': 'AS355GG675',
            'first_name': 'Jhon',
            'last_name': 'Soto'
        }
        user = User.objects.create_user(**self.jhon)
        self.user_global = user


        """Create 13 orders for pagination tests"""
        number_of_orders = 13
        for i in range(number_of_orders):
            Order.objects.create(created_by=user)

    def test_pagination_is_ten(self):
        self.client.force_login(self.user_global)
        resp = self.client.get('/orders/list/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['object_list']) == 10)

    def test_lists_all_products(self):
        """Get second page and confirm it has (exactly) remaining 3 items"""
        self.client.force_login(self.user_global)
        resp = self.client.get('/orders/list/?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['object_list']) == 3)




