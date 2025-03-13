from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Exercise  

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']  


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'reps', 'sets', 'weight']
        
