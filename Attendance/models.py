from django.db import models
from Employees.models import Employee

class Attendance(models.Model):
    employee = models.ForeignKey(Employee,
                                 on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField(null=True,
                                 blank=True)
    is_present = models.BooleanField(default=True)
    overtime_hours = models.DecimalField(max_digits=5,
                                         decimal_places=2,
                                         default=0)
    
    class Meta:
        unique_together = ['employee', 'date']