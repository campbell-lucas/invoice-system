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


class PaymentTerms(models.Model):
    payment_terms = models.CharField(max_length=100)

    def __str__(self):
        return self.payment_terms


class CustomerCountry(models.Model):
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.country


class Customer(models.Model):
    sales_manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sales_manager')
    collector = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='collector')
    number = models.PositiveIntegerField(validators=[validate_length])
    name = models.CharField(max_length=200)
    country = models.ForeignKey(CustomerCountry, on_delete=models.CASCADE, related_name='customer_country')
    bill_to_address = models.CharField(max_length=250)
    ship_to_address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    order_limit = models.IntegerField()
    credit_limit = models.IntegerField()
    credit_limit_currency_code = models.CharField(max_length=10)
    payment_terms = models.ForeignKey(PaymentTerms, on_delete=models.CASCADE, related_name='customer_payment_terms')
    slug = models.SlugField(blank=True, unique=True)
    password = models.CharField(_("password"), max_length=128)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        self.password = make_password(self.password)
        return super().save(*args, **kwargs)

