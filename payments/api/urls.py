"""
Payments Urls Api
"""

# Django Rest
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

# Views
from .views import *

app_name = 'api_payments'

router = SimpleRouter()

urlpatterns = [
    path('create/', CreatePaymentApiView.as_view(), name='create'),
]

urlpatterns += router.urls

urlpatterns = format_suffix_patterns(urlpatterns)
