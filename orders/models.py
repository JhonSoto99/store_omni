"""Orders model."""

import uuid

# Django
from django.db import models

# Models
from accounts.models import AuditBaseAbstract

# Signals
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Order(AuditBaseAbstract):
    """Orders model."""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.PositiveIntegerField(default=0)
    paid_out = models.BooleanField(
        'paid_out',
        default=False,
        help_text=(
            'Helps to easily distinguish the status pay order.'
        )
    )
    sent = models.BooleanField(
        default=False,
        help_text=(
            'Helps to easily distinguish the status Shipping order.'
        )
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
        return "{} - {} - {}".format(
            self.uuid,
            self.amount,
            self.created_by
        )


class OrderProducts(models.Model):
    """Order Products model."""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('order', 'product'),)

    def __str__(self):
        return '{} - {}: ${}'.format(
            self.order.uuid,
            self.product.name,
            self.order.amount
        )


@receiver(post_save, sender=OrderProducts)
def update_amount_order(sender, instance, created, **kwargs):
    """
    Signal post save for update amount for an order
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        order = Order.objects.get(uuid=instance.order.uuid)
        order.amount = order.amount+instance.product.price
        order.save()



