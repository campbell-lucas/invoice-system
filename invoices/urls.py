from django.urls import path

from . import views

app_name = 'invoices'

urlpatterns = [
    path('pdf/<int:number>/', views.render_pdf_view, name='render-pdf'),
    path('invoice/<int:number>', views.show_invoice, name='show-invoice'),
]
