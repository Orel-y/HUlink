from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher')
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
class Announcement(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="announcements")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} announced by {self.author.first_name}"