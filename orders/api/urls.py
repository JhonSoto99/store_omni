"""
Orders Urls Api
"""
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

# Views
from .views import *

app_name = 'api_orders'

router = SimpleRouter()

urlpatterns = [
    path('list/', OrderListView.as_view(), name='list'),
]

urlpatterns += router.urls

urlpatterns = format_suffix_patterns(urlpatterns)
