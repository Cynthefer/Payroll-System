from django.db import models
from Employees.models import Employee
from Salary.models import SalaryStructure

class Payroll(models.Model):
    employee = models.ForeignKey(Employee,
                                 on_delete=models.CASCADE,
                                 related_name='payrolls')
    month = models.IntegerField()#1-12
    year = models.IntegerField()
    salary_structure = models.ForeignKey(SalaryStructure,
                                         on_delete=models.SET_NULL,
                                         null=True)
    
    #Earnings
    basic = models.DecimalField(max_length=10,
                                decimal_places=2)
    hra = models.DecimalField(max_length=10,
                              decimal_places=2)
    travel = models.DecimalField(max_length=10,
                                 decimal_places=2)
    medical = models.DecimalField(max_length=10,
                                  decimal_places=2)
    other_earnings = models.DecimalField(max_length=10,
                                         decimal_places=2,
                                         default=0)
    overtime_pay = models.DecimalField(max_length=10,
                                       decimal_places=2,
                                       default=0)
    
    #Deductions
    provident_fund = models.DecimalField(max_length=10,
                                         decimal_places=2)
    professional_leave = models.DecimalField(max_length=10,
                                             decimal_places=2)
    leave_deductions = models.DecimalField(max_length=10,
                                           decimal_places=2,
                                           default=0)
    other_deductions = models.DecimalField(max_length=10,
                                           decimal_places=2,
                                           default=0)
    
    #Totals
    gross_earnings = models.DecimalField(max_length=10,
                                         decimal_places=2,
                                         editable=False)
    total_deductions = models.DecimalField(max_length=10,
                                           decimal_places=2,
                                           editable=False)
    net_salary = models.DecimalField(max_length=10,
                                     decimal_places=2,
                                     editable=False)
    
    class Meta:
        unique_together = ['employee', 'month', 'year']
    
    def save(self, *args, **kwargs):
        self.gross_earnings = self.basic + self.hra + self.travel + self.medical + self.other_earnings + self.overtime_pay
        self.total_deductions = self.provident_fund + self.professional_tax + self.leave_deductions + self.other_deductions
        self.net_salary = self.gross_earnings - self.total_deductions
        super().save(*args, **kwargs)