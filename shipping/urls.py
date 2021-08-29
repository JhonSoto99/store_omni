"""
 Shipping Urls
"""

# Django
from django.conf.urls import url, include
from django.urls import path

# Views
from .views import *

urlpatterns = [
    url(r'^list/', ShippingListView.as_view(), name="list"),

    path(
        route='create_shipping/',
        view=ShippingCreateView.as_view(),
        name='create'
    ),

    path(
        route='mark_received_shipping/<uuid:shipping_id>/',
        view=mark_received_shipping,
        name="mark_received_shipping"
    ),
]

