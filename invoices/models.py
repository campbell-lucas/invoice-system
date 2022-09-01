from django.db import models

from customers.models import validate_length, Customer


class Invoice(models.Model):

    PREPAYMENT = 'prepayment'
    NET_14 = '14 Days NET'
    NET_30 = '30 Days NET'
    NET_60 = '60 Days NET'
    NET_90 = '90 Days NET'
    PAID = 'PAID'
    CURRENT = 'CURRENT'
    OVERDUE = 'OVERDUE'

    PAYMENT_TERMS = (
        (PREPAYMENT, 'PREPAYMENT'),
        (NET_14, '14 DAYS NET'),
        (NET_30, '30 DAYS NET'),
        (NET_60, '60 DAYS NET'),
        (NET_90, '90 DAYS NET'),
    )

    STATUS_CHOICES = (
        (OVERDUE, 'OVERDUE'),
        (CURRENT, 'CURRENT'),
        (PAID, 'PAID'),
    )

    number = models.IntegerField(validators=[validate_length])
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    value = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(auto_now=True)
    payment_terms = models.CharField(choices=PAYMENT_TERMS)
    status = models.CharField(choices=STATUS_CHOICES, default="CURRENT")

    def __str__(self):
        return self.number
