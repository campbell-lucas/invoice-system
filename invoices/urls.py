from django.urls import path

from . import views

app_name = 'invoices'

urlpatterns = [
    path('pdf/<int:number>/', views.render_pdf_view, name='render-pdf'),
    path('create-invoice/', views.create_invoice_view, name='create-invoice'),
    path('add-invoice-products/', views.create_invoice_products, name='add-invoice-products'),
]
