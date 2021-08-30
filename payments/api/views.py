"""
Products Api Views
"""

# Django Restframework
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from payments.models import Payment
from orders.models import Order

# Serializers
from .serializer import PaymentSerializer



#Django
from django.db.models import Sum


class CreatePaymentApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, version):
        if not 'orders' in request.data:
            return Response([{
                'status': 'error',
                'msg': 'orders is required',
            }], status=status.HTTP_400_BAD_REQUEST)

        orders = request.data.getlist('orders')

        if orders:
            """
            the total value of the orders is obtained 
            to add them to the total value of the payment.
            """
            amount = Order.objects.filter(uuid__in=orders).aggregate(Sum('amount'))
            payment_created = Payment.objects.create(
                created_by=request.user,
                amount=amount['amount__sum']
            )

            payment_created.orders.add(*orders)
            payment_created.save()

            return Response({
                'results': PaymentSerializer(payment_created).data
            }, status=status.HTTP_200_OK)

        return Response({
            'results': 'success'
        }, status=status.HTTP_200_OK)