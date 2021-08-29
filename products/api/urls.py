"""
Products Urls Api
"""

# Django Rest
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

# Views
from .views import *

app_name = 'api_products'

router = SimpleRouter()
router.register(r"", ProductViewSet)

urlpatterns = [
    path('add_to_order/<uuid:product_id>/', ProductAddOrderApiView.as_view(), name='add_to_order'),
]

urlpatterns += router.urls

urlpatterns = format_suffix_patterns(urlpatterns)
