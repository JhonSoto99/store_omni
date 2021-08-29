"""Users URLs."""

# Django
from django.urls import path

# View
from .views import *

urlpatterns = [
    # Management
    path(
        route='login/',
        view=login_view,
        name='login'
    ),
    path(
        route='signup/',
        view=signup_view,
        name='signup'
    ),
    path(
        route='logout/',
        view=logout_view,
        name='logout'
    ),
]
