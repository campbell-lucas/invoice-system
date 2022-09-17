from django import forms

from invoices.models import Invoice, InvoiceProduct


class CreateInvoice(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ('customer', 'payment_terms', 'currency_code')

    def save(self, commit=True):
        invoice = super().save(commit=True)
        return invoice


class AddInvoiceProducts(forms.ModelForm):

    class Meta:
        model = InvoiceProduct
        fields = (
            'product',
            'quantity',
            'invoice'
        )

    def save(self, commit=True):
        product = super().save(commit=True)
        return product
