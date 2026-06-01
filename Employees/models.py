from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(max_length=50)
    contact = PhoneNumberField(unique=True)
    email = models.EmailField(max_length=254)
    ID = models.IntegerField(unique=True)
    employee_number = models.IntegerField(unique=True)
    position = models.CharField(max_length=50)
    salary = models.IntegerField()

    def __str__(self):
        return self.employee_number
    