from django.db import models

class SalaryStructure(models.Model):
    basic_salary = models.DecimalField(max_digits=10,
                                       decimal_places=2)
    house_rent_allowance = models.DecimalField(max_digits=10,
                                       decimal_places=2,
                                       default=0)
    travel_allowance = models.DecimalField(max_digits=10,
                                       decimal_places=2,
                                       default=0)
    medical_allowance = models.DecimalField(max_digits=10,
                                       decimal_places=2,
                                       default=0)
    other_allowances = models.DecimalField(max_digits=10,
                                       decimal_places=2,
                                       default=0)
    provident_fund = models.DecimalField(max_digits=10,
                                       decimal_places=2)#deduction
    professional_tax = models.DecimalField(max_digits=10,
                                       decimal_places=2,
                                       default=0)
    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['-effective_from']