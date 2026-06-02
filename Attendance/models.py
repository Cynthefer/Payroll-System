from django.db import models
from Employees.models import Employee

# Create your models here.
stat = (
    ('Good', 'Good'),
    ('Bad', 'Bad'),
)
type = (
    ("Annual", "Annual Leave"),
    ("Sick", "Sick Leave"),
    ("Paternity", "Maternity Leave"),
    ("Recovery", "Recovery Leave"),
    ("Family", "Family Responsibility Leave"),
)

leave_stat = (
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Rejected", "Rejected"),
)

class Attendance(models.Model):
    employee = models.ForeignKey(Employee , on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=stat, default="Good", max_length=50)

    def __str__(self):
        return self.status


class Leave_Request(models.Model):
    employee = models.ForeignKey(Employee , on_delete=models.CASCADE)
    leave_type = models.CharField(choices=type, default="Sick", max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(choices=leave_stat, default="Pending", max_length=50)
    