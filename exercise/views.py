from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Exercise
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
    return render(request, "login.html")

@login_required
def dashboard_view(request):
    exercises = Exercise.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"exercises": exercises})

@login_required
def track_exercise_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        reps = request.POST["reps"]
        sets = request.POST.get("sets", None)
        weight = request.POST.get("weight", None)
        Exercise.objects.create(user=request.user, name=name, reps=reps, sets=sets, weight=weight)
        return redirect("dashboard")
    return render(request, "track_exercise.html")

