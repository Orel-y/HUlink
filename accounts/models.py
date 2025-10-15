from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
        ('mentor', 'Mentor')
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.username} ({self.role})'


class Student(models.Model):
    user = models.OneToOneField(CustomUser,
                                on_delete=models.CASCADE,
                                related_name='student_profile')
    department = models.CharField(max_length=50)
    year_of_study = models.IntegerField(default=1)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Staff(models.Model):
    user = models.OneToOneField(CustomUser,
                                on_delete=models.CASCADE,
                                related_name='staff_profile')
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Mentor(models.Model):
    MentorStatusChoices = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('completed', 'Completed')
    )
    staff = models.ForeignKey(Staff,
                              on_delete=models.CASCADE,
                              related_name='mentor_staff')
    student = models.ForeignKey(Student,
                                on_delete=models.CASCADE,
                                related_name='mentor_student')
    status = models.CharField(max_length=20,
                              choices=MentorStatusChoices,
                              default='pending')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('staff', 'student')
