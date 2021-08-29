"""Products model."""

import uuid

# Django
from django.db import models

# Models
from accounts.models import AuditBaseAbstract


class Product(AuditBaseAbstract):
    """Products model."""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(
        max_length=50,
        help_text='Descriptive name.'
    )
    description = models.TextField(
        max_length=600,
    )
    price = models.PositiveIntegerField(default=0)
    enabled = models.BooleanField(
        default=True,
        help_text=(
            'Helps to easily distinguish the condition of the product.'
        )
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name