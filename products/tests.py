"""
Products test model.
"""

# Django
from django.db.utils import IntegrityError
from django.test import TestCase, RequestFactory
from rest_framework.test import force_authenticate

# Model
from .models import Product
from accounts.models import User
from orders.models import Order

# Views
from .views import ProductCreateView


class ProductTestCase(TestCase):
    """
        Test Models Products
    """
    def setUp(self):
        self.camera = {
            'name': 'camera',
            'description': 'dual camera',
            'price': 20000,
            'enabled': True
        }

        self.pc = {
            'name': 'MacBooc Pro',
            'description': '1tb ssd',
            'price': 3000000,
            'enabled': True
        }

    def test_create_product(self):
        product_camera = Product.objects.create(**self.camera)
        self.assertIsNotNone(product_camera.uuid)

    def test_disable_product(self):
        product_camera = Product.objects.create(**self.camera)
        product_camera.enabled=False
        product_camera.save()
        self.assertEqual(product_camera.enabled, False)


class ProductsViewTestCase(TestCase):
        """
        Test Views Products
        """
        def setUp(self):
            self.pc = {
                'name': 'MacBooc Pro',
                'description': '1tb ssd',
                'price': 3000000,
                'enabled': True
            }
            self.jhon = {
                'username': 'jhon@gmail.com',
                'password': 'AS355GG675',
                'first_name': 'Jhon',
                'last_name': 'Soto'
            }

            """Create 13 products for pagination tests"""
            number_of_products = 13
            for i in range(number_of_products):
                Product.objects.create(**self.pc)

        def test_create_product(self):
            user = User.objects.create_user(**self.jhon)
            self.client.force_login(user)
            request = self.client.post('/products/create/', self.pc)
            self.assertEqual(request.status_code, 302)
            self.assertEqual(request.url, "/products/list/")

        def test_pagination_is_ten(self):
            user = User.objects.create_user(**self.jhon)
            self.client.force_login(user)
            resp = self.client.get('/products/list/')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue(len(resp.context['object_list']) == 10)

        def test_lists_all_products(self):
            """Get second page and confirm it has (exactly) remaining 3 items"""
            user = User.objects.create_user(**self.jhon)
            self.client.force_login(user)
            resp = self.client.get('/products/list/?page=2')
            self.assertEqual(resp.status_code, 200)
            self.assertTrue('is_paginated' in resp.context)
            self.assertTrue(resp.context['is_paginated'] == True)
            self.assertTrue(len(resp.context['object_list']) == 3)

        def test_update_product(self):
            product = Product.objects.create(**self.pc)
            user = User.objects.create_user(**self.jhon)
            self.client.force_login(user)
            resp = self.client.put(f'/products/edit/{product.uuid}/',
                                   {
                                       'name:': 'NewName',
                                       'description': 'New Description',
                                       'price': 0,
                                       'enabled': True
                                   })
            self.assertEqual(resp.status_code, 200)

        def test_delete_product(self):
            product = Product.objects.create(**self.pc)
            user = User.objects.create_user(**self.jhon)
            self.client.force_login(user)
            resp = self.client.delete(f'/products/delete/{product.uuid}/')
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.url, "/products/list/")

        def add_product_to_order(self):
            product = Product.objects.create(**self.pc)
            order = Order.objects.create(created_by=user)
            user = User.objects.create_user(**self.jhon)
            self.client.force_login(user)
            resp = self.client.delete(f'/products/add_product_order_select/{product.uuid}/',
                                      {
                                          'order': order.uuid
                                      })
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.url, "/products/list/")

            """Validate if amount order is updated"""
            order_updated = Order.objects.get(uuid=order.uuid)
            self.assertNotEqual(order_updated.amount, 0)




