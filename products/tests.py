"""
Products test model.
"""

# Django
from django.db.utils import IntegrityError
from django.test import TestCase

# Model
from .models import Product


class ProductTestCase(TestCase):

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


