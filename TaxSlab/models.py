from django.db import models

class TaxSlab(models.Model):
    financial_year = models.CharField(max_length=20)
    min_income = models.DecimalField(max_digits=10,
                                     decimal_places=2)
    max_income = models.DecimalField(max_digits=10,
                                     decimal_places=2,
                                     null=True,
                                     blank=True)
    tax_rate = models.DecimalField(max_digits=5,
                                   decimal_places=2)#percentage
    cess = models.DecimalField(max_digits=5,
                               decimal_places=2,
                               default=0)