# Generated by Django 4.1 on 2022-09-07 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='TestPass123', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
