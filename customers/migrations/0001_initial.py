# Generated by Django 4.0.4 on 2022-09-02 18:46

import customers.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(validators=[customers.models.validate_length])),
                ('name', models.CharField(max_length=200)),
                ('customer_country', models.CharField(max_length=200)),
                ('bill_to_address', models.CharField(max_length=250)),
                ('ship_to_address', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('order_limit', models.IntegerField()),
                ('credit_limit', models.IntegerField()),
                ('credit_limit_currency_code', models.CharField(max_length=10)),
                ('payment_terms', models.CharField(choices=[('prepayment', 'Prepayment'), ('14 Days NET', '14 Days NET'), ('30 Days NET', '30 Days NET'), ('60 Days NET', '60 Days NET'), ('90 Days NET', '90 Days NET')], default='30 Days NET', max_length=100)),
                ('collector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collector', to=settings.AUTH_USER_MODEL)),
                ('sales_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_manager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
