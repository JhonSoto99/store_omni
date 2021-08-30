"""Products Views."""

# Django
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from .models import *


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    queryset = model.objects.all()
    template_name = 'orders/list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        if not self.request.user.is_superuser or not self.request.user.is_staff:
            """
            Filter Order by created_by if is an
            user no privileges admin 
            """
            queryset = queryset.filter(
                created_by=self.request.user
            )
        return queryset




