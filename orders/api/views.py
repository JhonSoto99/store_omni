"""
Products Api Views
"""

# Django Restframework
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.generics import ListAPIView

# Models
from orders.models import Order, OrderProducts

# Serializers
from .serializer import OrderSerializer

# Pagination
from store_omni.pagination import StandardResultsSetPagination


class OrderListView(ListAPIView):
    """
        View for management crud at Orders
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Order.objects.all()
        if not self.request.user.is_superuser or not self.request.user.is_staff:
            queryset = queryset.filter(
                created_by=self.request.user
            )

        return queryset