"""Payments Views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.views.generic.list import ListView

# Models
from .models import *
from orders.models import *

# Forms
from .forms import ShippingForm

# Celery
from .tasks import send_notification

class ShippingListView(LoginRequiredMixin, ListView):
    model = Shipping
    queryset = model.objects.all()
    template_name = 'shipping/list.html'
    paginate_by = 10


class ShippingCreateView(LoginRequiredMixin, CreateView):
    model = Shipping
    form_class = ShippingForm
    template_name = 'shipping/create.html'

    def form_valid(self, form, **kwargs):
        """
        Validate and save
        """
        if form.is_valid():
            orders = form.cleaned_data.get("orders")

            shipping_created = Shipping.objects.create(
                created_by=self.request.user,
            )

            shipping_created.orders.add(*list(orders))
            shipping_created.save()

            """Send notification with Celery to User"""
            list_email_users = shipping_created.orders.all().values_list('created_by__email', flat=True)
            send_notification.delay(list(list_email_users), "Has sent your products")

            msg = 'Order sent and notify successfully.'
            messages.info(
                self.request,
                msg
            )

            return HttpResponseRedirect(reverse('shipping:list'))


    def get_context_data(self, **kwargs):
        context = super(ShippingCreateView, self).get_context_data(**kwargs)
        context['exists_orders_to_send'] = Order.objects.filter(
            sent=False
        )
        return context


def mark_received_shipping(request, shipping_id):
    """
    Method for method to mark a shipment as received and notify the user
    """
    shipping = Shipping.objects.get(uuid=shipping_id)
    shipping.received = True
    shipping.save()

    """Send notification with Celery to User"""
    list_email_users = shipping.orders.all().values_list('created_by__email', flat=True)
    send_notification.delay(list(list_email_users), "We are happy that you received your products")

    msg = 'Shipping marks as received successfully.'
    messages.info(
        request,
        msg
    )

    return HttpResponseRedirect(reverse('shipping:list'))
