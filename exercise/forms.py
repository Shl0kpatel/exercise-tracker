from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Exercise  # Import CustomUser instead of auth.User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']  # Ensure email is included


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'reps', 'sets', 'weight']
