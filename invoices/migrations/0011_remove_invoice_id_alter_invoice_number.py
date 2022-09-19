# Generated by Django 4.1 on 2022-09-14 20:23

import customers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0010_alter_invoice_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='id',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[customers.models.validate_length]),
        ),
    ]