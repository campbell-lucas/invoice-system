from django.db import models


class Collector(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
