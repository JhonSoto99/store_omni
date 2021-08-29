"""
Accounts Api Urls
"""

# Django
from django.urls import path, include
from django.contrib.auth.models import User
from django.conf.urls import url

# Django Rest Framework
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns

# Views Api
from .views import SignupAPIView, UserRetrieveAPIView

app_name = "api_accounts"

# Routes
urlpatterns = [
    url(r'^signup/$', SignupAPIView.as_view(), name="signup"),
    url(r'^profile/$', UserRetrieveAPIView.as_view(), name="profile"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
