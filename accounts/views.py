"""Users views."""

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.urls import reverse
from django.shortcuts import render, redirect

# Models
from .models import User

# Forms
from .forms import SignupForm


def login_view(request):
    """Login a user."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('products:list')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'invalid username and password'
            })

    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))


def signup_view(request):
    """Sign up a user."""
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                is_superuser=False,
                is_staff=False
            )
            new_user.save()
            login(request, new_user)
            return redirect('products:list')

    return render(request, 'accounts/signup.html', context={
        'form': form
    })
