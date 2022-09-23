from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission, Group
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . import forms


def registration_view(request):
    """
    this view is used for creating customers
    """
    form = forms.RegistrationForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()

            return redirect(reverse_lazy('home:home'))
    return render(request, 'users/registration.html', {'form': form})
