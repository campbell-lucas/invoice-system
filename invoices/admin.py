from django.contrib import admin

from . import models

admin.site.register(models.Invoice)
admin.site.register(models.InvoiceStatus)
admin.site.register(models.InvoiceProduct)
admin.site.register(models.Product)
admin.site.register(models.CurrencyCode)
