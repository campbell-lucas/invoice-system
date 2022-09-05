from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission, Group
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . import forms


def registration_view(request):
    form = forms.RegistrationForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()

            # if form.cleaned_data.get('is_instructor') is True:
            #     permission = Permission.objects.get(name='Can add course')
            #     instructor_group = Group.objects.get(name='instructors')
            #     user.groups.add(instructor_group)
            #     user.user_permissions.add(permission)
            # else:
            #     permission = Permission.objects.get(name='Can view course')
            #     students_group = Group.objects.get(name='students')
            #     user.groups.add(students_group)
            #     user.user_permissions.add(permission)

            return redirect(reverse_lazy('home:home'))
    return render(request, 'users/registration.html', {'form': form})
