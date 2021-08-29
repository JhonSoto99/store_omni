"""Payments model."""

import uuid

# Django
from django.db import models
from django.db.models import Sum

# Models
from accounts.models import AuditBaseAbstract
from products.models import Product

# Signals
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Payment(AuditBaseAbstract):
    """Payment model."""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.PositiveIntegerField(default=0)
    orders = models.ManyToManyField('orders.Order', related_name='payment_orders')
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
            self.amount
        )


@receiver(post_save, sender=Payment)
def update_order_and_payment(sender, instance, created, **kwargs):
    """
    Signal post save for update status orders and ammount at payments
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    for order in instance.orders.all():
        order.paid_out = True
        order.save()