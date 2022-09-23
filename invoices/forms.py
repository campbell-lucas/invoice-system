from django import forms

from invoices.models import Invoice, InvoiceProduct


class CreateInvoice(forms.ModelForm):
    """
    this class is used to create the form for creating invoices
    """

    class Meta:
        model = Invoice
        fields = ('customer', 'payment_terms', 'currency_code')

    def save(self, commit=True):
        invoice = super().save(commit=True)
        return invoice


class AddInvoiceProducts(forms.ModelForm):
    """
    this class is used to show the fields needed to add products to invoices
    """

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
