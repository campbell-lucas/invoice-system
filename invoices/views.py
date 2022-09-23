from datetime import date, timedelta

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.defaultfilters import slugify
from django.template.loader import get_template
from django.urls import reverse_lazy
from xhtml2pdf import pisa

from invoices import forms
from invoices.models import Invoice, InvoiceProduct
from customers.models import Customer


def render_pdf_view(request, number):
    """
    this function is used to generate pdfs
    """
    invoice = Invoice.objects.get(number=number)
    invoice_items = InvoiceProduct.objects.filter(invoice=number)
    for product in invoice_items:
        total = product.product.price * product.quantity
        quantity = product.quantity
    template_path = 'invoices/invoice.html'
    context = {'invoice': invoice, 'total': total, 'invoice_items': invoice_items, 'quantity': quantity}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{invoice}.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def create_invoice_view(request):
    """
    this function is used in creating the invoices
    """
    form = forms.CreateInvoice(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.slug = slugify(invoice.number)

            if invoice.payment_terms_id == 1:
                invoice.due_date = (date.today() + timedelta(days=0))
            if invoice.payment_terms_id == 2:
                invoice.due_date = (date.today() + timedelta(days=14))
            if invoice.payment_terms_id == 3:
                invoice.due_date = (date.today() + timedelta(days=30))
            if invoice.payment_terms_id == 4:
                invoice.due_date = (date.today() + timedelta(days=60))
            if invoice.payment_terms_id == 5:
                invoice.due_date = (date.today() + timedelta(days=90))

            if invoice.today_date >= invoice.due_date:
                invoice.status_id = 2
            else:
                invoice.status_id = 3

            invoice.save()

            return redirect(reverse_lazy('invoices:add-invoice-products'))
    return render(request, 'invoices/create_invoice.html', {'form': form})


def create_invoice_products(request):
    """
    this function is used to add products to the invoices
    """
    form = forms.AddInvoiceProducts(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            product = form.save(commit=False)

            product.save()

            return redirect(reverse_lazy('home:customer-list'))
    return render(request, 'invoices/add_invoice_products.html', {'form': form})
