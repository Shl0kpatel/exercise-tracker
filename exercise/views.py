from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, ExerciseForm
from .models import Exercise
from .models import CustomUser


from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            if CustomUser.objects.filter(email=email).exists():
                form.add_error("email", "This email is already registered.")
            else:
                form.save()
                return redirect("login")  # Redirect to login after successful registration
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})



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
    e = Exercise.objects.filter(user=request.user)  # Fetch only user's exercises
    return render(request, 'dashboard.html', {'exercises': e})

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

@login_required
def delete_exercise(request, id):
    e = get_object_or_404(Exercise, id=id, user=request.user)  # Ensure user owns exercise
    e.delete()
    return redirect('dashboard')  # Redirect back to dashboard

def edit_exercise(request, exercise_id):
    e = get_object_or_404(Exercise, id=exercise_id)
    
    if request.method == 'POST':
        f = ExerciseForm(request.POST, instance=e)
        if f.is_valid():
            f.save()
            return redirect('dashboard')  # Redirect to tracked exercises page

    else:
        f = ExerciseForm(instance=e)

    return render(request, 'edit_exercise.html', {'form': f})
