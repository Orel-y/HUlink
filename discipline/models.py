# community/models.py (or create a new app named 'discipline' if you prefer modularity)
from django.db import models
from accounts.models import CustomUser, Staff, Student
from django.utils import timezone

class DisciplineReport(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='discipline_reports')
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True, related_name='discipline_reports')  # Assigned staff who reviews
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.student.user.username} ({self.status})"
