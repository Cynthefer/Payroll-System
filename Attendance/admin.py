from django.contrib import admin
from .models import Attendance, Leave_Request

# Register your models here.
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'check_in', 'check_out', 'status')
    list_filter = ('employee', 'date', 'status')
    search_fields = ('employee', 'date', 'status')

@admin.register(Leave_Request)
class Leave_RequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave_type', 'applied', 'start_date', 'end_date', 'status')
    list_filter = ('employee', 'leave_type', 'applied', 'status')
    search_fields = ('employee', 'leave_type', 'reason')
