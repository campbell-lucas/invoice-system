# Generated by Django 4.1 on 2022-09-03 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]