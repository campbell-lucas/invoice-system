from django.urls import path

from . import views

app_name = 'customers'

urlpatterns = [
    path('create/', views.CreateCustomerView.as_view(), name='create-customer'),
    path('customers/', views.CustomerView.as_view(), name='customer_list'),
    path('customers/<slug:slug>', views.CustomerDetailView.as_view(), name='customer_detail_view'),
]
