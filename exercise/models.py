from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add other fields as needed

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    # Define user types
    USER_TYPE_CHOICES = (
        ('user', 'User'),
        ('trainer', 'Trainer'),
        ('admin', 'Admin'),
    )

    # Add a field to store the user type
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')


    def __str__(self):
        return self.username