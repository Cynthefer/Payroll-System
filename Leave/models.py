from django.db import models

class Leave(models.Model):
    LEAVE_TYPES = [
        ('SL', 'Sick Leave'),
        ('PL', 'Paid Leave'),
        ('UL', 'Unpaid Leave'),
        ('AL', 'Annual Leave'),
        ('ML', 'Maternity Leave'),
        ('PL', 'Paternity Leave'),
        ('FRL', 'Family Responsibilty Leave'),
    ]
    LEAVE_STATUS = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
    ]
    leave_type = models.CharField(max_length=5,
                                  choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    attachments = models.FileField(upload_to='Leave/Attachments',
                                   max_length=100)
    status =models.CharField(max_length=20, choices=LEAVE_STATUS,
                             default='P')