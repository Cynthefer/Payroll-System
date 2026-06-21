from django.db import models
from Employees.models import Employee

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100, unique=True)
    manager = models.ForeignKey(Employee,
                                on_delete=models.SET_NULL,
                                null=True,
                                related_name='managed_department')
    def __str__(self):
        return self.name
    