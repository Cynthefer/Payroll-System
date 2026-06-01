from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'employee_number', 'ID')
    search_fields = ('ID', 'employee_number', 'contact', 'email')
    pass
