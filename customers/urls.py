from django.urls import path

from . import views

app_name = 'customers'

urlpatterns = [
    path('create/', views.CreateCustomerView.as_view(), name='create-customer'),
]
