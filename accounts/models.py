"""
User model
"""

# Django
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    User model.
    Extend from Django's Abstract User,
    change the username field to email.
    Author: Jhon Soto
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


# ABSTRACTS MODEL
class AuditBaseAbstract(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created date',
        help_text='created date',
        null=True,
        editable=False
    )
    changed_at = models.DateTimeField(
        auto_now=True,
        verbose_name='updated date',
        help_text='updated date',
        null=True,
        editable=False
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        editable=False
    )

    created_by = models.ForeignKey(
        'accounts.User',
        verbose_name="Created by",
        help_text="Who created it?",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="%(class)s_created_by",
        editable=False
    )
    changed_by = models.ForeignKey(
        'accounts.User',
        verbose_name="Changed by",
        help_text="Who changed it?",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="%(class)s_changed_by",
        editable=False
    )

    class Meta:
        abstract = True
