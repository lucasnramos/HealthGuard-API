from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ComplianceRequirement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Document(models.Model):
    requirement = models.ForeignKey(ComplianceRequirement, on_delete=models.CASCADE)
    file_path = models.FileField(upload_to='documents/')
    status = models.CharField(max_length=20)  # e.g., 'submitted', 'approved', 'rejected'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
