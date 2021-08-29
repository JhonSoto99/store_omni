from django.conf.urls import url, include

from .views import *

urlpatterns = [
    url(r'^list/', OrderListView.as_view(), name="list"),
]

