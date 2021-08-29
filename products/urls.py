"""
 Products Urls
"""

# Django
from django.conf.urls import url, include
from django.urls import path

# Views
from .views import *

urlpatterns = [
    url(r'^create/', ProductCreateView.as_view(), name="create"),
    url(r'^list/', ProductListView.as_view(), name="list"),
    path(
        route='add_product_order_select/<uuid:product_id>/',
        view=ProductOrderCreateView.as_view(),
        name='add_product_order_select'
    ),
    path(
        route='edit/<pk>/',
        view=ProductsUpdateView.as_view(),
        name='edit'
    ),
    path(
        route='delete/<pk>/',
        view=ProductsDeleteView.as_view(),
        name='delete'
    ),
    path(
        route='products/<uuid:product_id>/add_product_order_default/',
        view=add_product_order_default,
        name='add_product_order_default'
    ),
    path(
        route='check_exists_order/<uuid:product_id>/',
        view=check_exists_order,
        name="check_exists_order"
    ),
]

