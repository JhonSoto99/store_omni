"""Payments Views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.db.models import Sum

# Models
from .models import *
from orders.models import *


# Forms
from .forms import PaymentForm

class PayOrdersCreateView(LoginRequiredMixin, CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payments/pay_orders.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs


    def form_valid(self, form, **kwargs):
        """
        Validate and save
        """
        if form.is_valid():
            orders = form.cleaned_data.get("orders")
            amount = orders.aggregate(Sum('amount'))

            payment_created = Payment.objects.create(
                created_by=self.request.user,
                amount=amount['amount__sum']
            )

            payment_created.orders.add(*list(orders))
            payment_created.save()

            msg = 'Payment made successfully.'
            messages.info(
                self.request,
                msg
            )

            return HttpResponseRedirect(reverse('orders:list'))


    def get_context_data(self, **kwargs):
        context = super(PayOrdersCreateView, self).get_context_data(**kwargs)
        context['exists_orders_to_pay'] = Order.objects.filter(
            created_by=self.request.user,
            paid_out=False
        ).exists()
        return context
