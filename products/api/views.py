"""
Products Api Views
"""

# Django Restframework
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from products.models import Product
from orders.models import Order, OrderProducts

# Serializers
from .serializer import ProductSerializer

# Pagination
from store_omni.pagination import StandardResultsSetPagination

#Djanfo
from django.db import IntegrityError


class ProductViewSet(ModelViewSet):
    """
        View for management crud at Products
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request, version):
        queryset = self.queryset
        if not self.request.user.is_superuser or not self.request.user.is_staff:
            queryset = queryset.filter(
                enabled=True
            )

        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.serializer_class(result_page, many=True, context={'user': request.user})

        return paginator.get_paginated_response(serializer.data)


class ProductAddOrderApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, version, product_id):
        user_order = Order.objects.filter(
            created_by=request.user,
            paid_out=False,
            sent=False,
        ).first()
        product = Product.objects.get(uuid=product_id)

        if user_order:
            try:
                OrderProducts.objects.create(
                    order=user_order,
                    product=product
                )
            except IntegrityError:
                return Response([{
                    'status': 'error',
                    'msg': 'product already exists at order user',
                }], status=status.HTTP_400_BAD_REQUEST)
        else:
            order_created = Order.objects.create(
                created_by=request.user
            )

            try:
                OrderProducts.objects.create(
                    order=order_created,
                    product=product
                )
            except IntegrityError:
                return Response([{
                    'status': 'error',
                    'msg': 'product already exists at order user',
                }], status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'results': 'Success'
        }, status=status.HTTP_200_OK)