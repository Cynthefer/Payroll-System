from django.contrib import admin
from .models import Employee, Department, Position, Bank_Details

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'employee_number', 'ID')
    list_filter = ('first_name', 'last_name', 'employee_number' , 'ID', 'position' )
    search_fields = ('ID', 'employee_number', 'contact', 'email')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_of_dept', 'code')
    list_filter = ('name', 'head_of_dept', 'code')
    search_fields = ('name', 'head_of_dept', 'code')

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'grade', 'base_salary_range')
    search_fields = ('title', 'grade')

@admin.register(Bank_Details)
class Bank_DetailsAdmin(admin.ModelAdmin):
    search_fields = ('account_number',)
