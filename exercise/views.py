from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ExerciseForm
from .models import Exercise

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.level = "Beginner"  # Set a default level manually
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
    return render(request, 'login.html')

@login_required
def dashboard(request):
    exercises = Exercise.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'exercises': exercises})

@login_required
def track_exercise(request):
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.user = request.user
            exercise.save()
            return redirect('dashboard')  # Redirect back to dashboard after tracking exercise
    else:
        form = ExerciseForm()
    return render(request, 'track_exercise.html', {'form': form})

from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
