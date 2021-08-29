"""
Accounts test model.
"""

# Django
from django.db.utils import IntegrityError
from django.test import TestCase

# Model
from .models import User


class CreateUserTestCase(TestCase):

    def setUp(self):
        self.jhon = {
            'email': 'jhon@gmail.com',
            'password': 'AS355GG675',
            'first_name': 'Jhon',
            'last_name': 'Soto'
        }

        self.alan = {
            'email': 'jhon@gmail.com',
            'password': '123EDFTR678',
            'first_name': 'Alan',
            'last_name': 'Soto'
        }

    def test_create_user(self):
        user_jhon = User.objects.create(**self.jhon)
        self.assertIsNotNone(user_jhon.id)

    def test_create_user_unique_email(self):
        """Proof that you cannot create a user with the same email."""
        User.objects.create(**self.alan)
        with self.assertRaises(Exception) as raised:
            User.objects.create(**self.alan)
        # Raise exception duplicate key value violates unique constraint
        self.assertEqual(IntegrityError, type(raised.exception))


