from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('customer-list/', views.HomeView.as_view(), name='customer-list'),
    path('contact/<int:pk>/', views.send_email, name='send_email'),
]
