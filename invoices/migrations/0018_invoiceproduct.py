# Generated by Django 4.1 on 2022-09-15 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0017_remove_product_invoice_remove_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.invoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.product')),
            ],
        ),
    ]
