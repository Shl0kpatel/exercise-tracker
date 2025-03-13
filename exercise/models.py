from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now  
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)  
    level = models.CharField(max_length=50, default="Beginner")

class Exercise(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    name = models.CharField(max_length=100)
    reps = models.IntegerField()
    sets = models.IntegerField(default=1)
    weight = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"
    

