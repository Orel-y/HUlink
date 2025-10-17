from django.db import models
from accounts.models import CustomUser

class Petition(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('resolved', 'Resolved'),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="petitions")
    is_anonymous = models.BooleanField(default=False)
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.status})"


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='announcements')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.created_by.username}"


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                             related_name='comments')
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE,
                                 related_name='comments',
                                 null=True, blank=True)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE,
                                 related_name='comments',
                                 null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username}"