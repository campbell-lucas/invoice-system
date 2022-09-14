# Generated by Django 4.1 on 2022-09-09 20:50

import customers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customer_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='number',
            field=models.PositiveIntegerField(unique=True, validators=[customers.models.validate_length]),
        ),
    ]
