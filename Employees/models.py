from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)
    head_of_dept = models.CharField(max_length=50)
    code = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    

class Position(models.Model):
    title = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    base_salary_range = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

class Bank_Details(models.Model):
    account_number = models.PositiveIntegerField()
    ifsc_code = models.PositiveIntegerField()
    employee_relation = models.CharField(max_length=50)

    def __str__(self):
        return self.account_number
    

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(max_length=50)
    contact = PhoneNumberField(unique=True)
    email = models.EmailField(max_length=254)
    ID = models.IntegerField(unique=True)
    employee_number = models.IntegerField(unique=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    banking = models.ForeignKey(Bank_Details, on_delete=models.CASCADE)
    department = models.ForeignKey(Department ,on_delete=models.CASCADE)

    class Meta:
        db_table = "Employees"
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ["last_name", "first_name", "ID"]

    def __str__(self):
        return self.employee_number
    