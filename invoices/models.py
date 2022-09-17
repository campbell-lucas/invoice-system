from django.db import models
from django.utils.text import slugify

from customers.models import Customer, PaymentTerms


class Product(models.Model):
    product = models.CharField(max_length=200)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.product


class CurrencyCode(models.Model):
    currency_code = models.CharField(max_length=10)

    def __str__(self):
        return self.currency_code


class InvoiceStatus(models.Model):
    status = models.CharField(max_length=150)

    def __str__(self):
        return self.status


class Invoice(models.Model):
    number = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoice_customer')
    value = models.IntegerField(blank=True, null=True)
    order_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    payment_terms = models.ForeignKey(PaymentTerms, on_delete=models.CASCADE, related_name='invoice_payment_terms')
    status = models.ForeignKey(InvoiceStatus, on_delete=models.CASCADE, null=True, related_name='invoice_status')
    slug = models.SlugField(blank=True, unique=True)
    today_date = models.DateField(auto_now=True)
    currency_code = models.ForeignKey(CurrencyCode, on_delete=models.CASCADE, related_name='invoice_currency_code',
                                      default='EUR')
    products = models.ManyToManyField(Product, through='InvoiceProduct')

    def __str__(self):
        return str(self.number)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.number)
        return super().save(*args, **kwargs)


class InvoiceProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='invoice_product')
    quantity = models.IntegerField()
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice_product')

    def __str__(self):
        return self.product.product

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
