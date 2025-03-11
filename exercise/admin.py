from django.contrib import admin
from .models import CustomUser, Exercise

admin.site.register(CustomUser)
admin.site.register(Exercise)
