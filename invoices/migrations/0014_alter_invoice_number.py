# Generated by Django 4.1 on 2022-09-14 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0013_alter_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
