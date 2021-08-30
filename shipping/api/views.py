"""
Shipping Api Views
"""

# Django Restframework
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

# Models
from shipping.models import Shipping

# Serializers
from .serializer import ShippingSerializer

# Celery
from shipping.tasks import send_notification


class CreateShippingApiView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, version):
        if not 'orders' in request.data:
            return Response([{
                'status': 'error',
                'msg': 'orders is required',
            }], status=status.HTTP_400_BAD_REQUEST)

        orders = request.data.getlist('orders')

        if orders:
            shipping_created = Shipping.objects.create(
                created_by=request.user
            )

            shipping_created.orders.add(*orders)
            shipping_created.save()

            """Send notification with Celery to User"""
            list_email_users = shipping_created.orders.all().values_list('created_by__email', flat=True)
            send_notification.delay(list(list_email_users), "Has sent your products")

            return Response({
                'results': ShippingSerializer(shipping_created).data
            }, status=status.HTTP_200_OK)

        return Response({
            'results': 'success'
        }, status=status.HTTP_200_OK)