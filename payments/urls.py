"""
 Payment Urls
"""

# Django
from django.conf.urls import url, include
from django.urls import path

# Views
from .views import *

urlpatterns = [
    path(
        route='pay_orders/',
        view=PayOrdersCreateView.as_view(),
        name='pay_orders'
    ),
]

