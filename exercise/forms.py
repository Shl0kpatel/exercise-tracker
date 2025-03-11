from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Exercise  # Import CustomUser instead of auth.User

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use CustomUser instead of auth.User
        fields = ['username', 'password1', 'password2']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'reps', 'sets', 'weight']
