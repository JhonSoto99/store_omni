"""Shipping model."""

import uuid

# Django
from django.db import models

# Models
from accounts.models import AuditBaseAbstract

# Signals
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Shipping(AuditBaseAbstract):
    """Shipping model."""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    orders = models.ManyToManyField('orders.Order', related_name='shipping_orders')
    received = models.BooleanField(
        default=False
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

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return "{} - {}".format(
            self.uuid,
            self.created_by,
        )

@receiver(post_save, sender=Shipping)
def update_order(sender, instance, created, **kwargs):
    """
    Signal post save for update status orders  at shipping
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    for order in instance.orders.all():
        order.sent = True
        order.save()
