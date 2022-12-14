# Generated by Django 4.1 on 2022-09-15 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0019_currencycode_invoice_products_alter_invoice_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='currency_code',
            field=models.ForeignKey(default='EUR', on_delete=django.db.models.deletion.CASCADE, related_name='invoice_currency_code', to='invoices.currencycode'),
        ),
    ]
