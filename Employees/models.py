#django imports
from django.db import models
from django.contrib.auth.models import User

#third party imports
from phonenumber_field.modelfields import PhoneNumberField

#other application imports
from Leave.models import Leave
from TaxSlab.models import TaxSlab
from Payroll.models import Payroll
from Attendance.models import Attendance
from Department.models import Department

class Employee(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20,
                                   unique=True,
                                   primary_key=True)
    id_number = models.IntegerField()
    contact = PhoneNumberField()
    alt_contact = PhoneNumberField()
    account_number = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=20)
    pan_number = models.CharField(max_length=50,
                                  unique=True)
    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE)
    attendance = models.ForeignKey(Attendance,
                                   on_delete=models.CASCADE)
    leave = models.ForeignKey(Leave,
                              on_delete=models.CASCADE)
    payroll = models.ForeignKey(Payroll,
                                on_delete=models.CASCADE)
    tax = models.ForeignKey(TaxSlab,
                           on_delete=models.CASCADE)
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)
    people = models.Manager()
    
    class Meta:
        db_table = 'Employees'
        verbose_name_plural = 'Employees'
    
    def __str__(self):
        return self.employee_id