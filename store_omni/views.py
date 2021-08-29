"""Menus views."""

# Django
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def home_view(request):
    """Page home view."""
    return render(request, 'accounts/login.html')

def not_found_view(request):
    """Page not found view."""
    return render(request, 'store/errors/404.html')


def server_error_view(request):
    """Internal server error view."""
    return render(request, 'store/errors/500.html')
