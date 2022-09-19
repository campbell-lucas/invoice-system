# Generated by Django 4.1 on 2022-09-15 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_customer_number'),
        ('invoices', '0018_invoiceproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='products',
            field=models.ManyToManyField(through='invoices.InvoiceProduct', to='invoices.product'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_customer', to='customers.customer'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_terms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_payment_terms', to='customers.paymentterms'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_status', to='invoices.invoicestatus'),
        ),
        migrations.AlterField(
            model_name='invoiceproduct',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_product', to='invoices.invoice'),
        ),
        migrations.AlterField(
            model_name='invoiceproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_product', to='invoices.product'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='currency_code',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_currency_code', to='invoices.currencycode'),
        ),
    ]