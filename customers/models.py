from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.db import models
from users.models import CustomUser


def validate_length(value):
    length = len(str(value))
    if length > 6:
        raise ValidationError(
            _(f'{value} is longer than 6 digits')
        )


class Customer(models.Model):

    PREPAYMENT = 'prepayment'
    NET_14 = '14 Days NET'
    NET_30 = '30 Days NET'
    NET_60 = '60 Days NET'
    NET_90 = '90 Days NET'

    PAYMENT_TERMS = (
        (PREPAYMENT, 'Prepayment'),
        (NET_14, '14 Days NET'),
        (NET_30, '30 Days NET'),
        (NET_60, '60 Days NET'),
        (NET_90, '90 Days NET'),
    )

    sales_manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sales_manager')
    collector = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='collector')
    number = models.PositiveIntegerField(validators=[validate_length])
    name = models.CharField(max_length=200)
    customer_country = models.CharField(max_length=200)
    bill_to_address = models.CharField(max_length=250)
    ship_to_address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    order_limit = models.IntegerField()
    credit_limit = models.IntegerField()
    credit_limit_currency_code = models.CharField(max_length=10)
    payment_terms = models.CharField(choices=PAYMENT_TERMS, default=NET_30, max_length=100)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
