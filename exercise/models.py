from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now  

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)  # Ensure email is required
    level = models.CharField(max_length=50, default="Beginner")


class Exercise(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    name = models.CharField(max_length=100)  
    reps = models.PositiveIntegerField()  # No default value
    sets = models.PositiveIntegerField(null=True, blank=True)  
    weight = models.FloatField(null=True, blank=True)  
    date = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return f"{self.name} - {self.user.username}"
