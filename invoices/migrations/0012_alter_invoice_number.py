# Generated by Django 4.1 on 2022-09-14 20:24

import customers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0011_remove_invoice_id_alter_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=models.AutoField(primary_key=True, serialize=False, validators=[customers.models.validate_length]),
        ),
    ]