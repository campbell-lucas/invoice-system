from django.db import models
from django.utils.text import slugify

from customers.models import validate_length, Customer, PaymentTerms


class InvoiceStatus(models.Model):
    status = models.CharField(max_length=150)

    def __str__(self):
        return self.status


class Invoice(models.Model):

    number = models.IntegerField(validators=[validate_length])
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    value = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(auto_now=True)
    payment_terms = models.ForeignKey(PaymentTerms, on_delete=models.CASCADE)
    status = models.ForeignKey(InvoiceStatus, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return str(self.number)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.number)
        return super().save(*args, **kwargs)
