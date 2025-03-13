from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Serve the home page as default
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('track/', views.track_exercise, name='track_exercise'),
    path('logout/', views.user_logout, name='logout'),
    path('delete_exercise/<int:id>/', views.delete_exercise, name='delete_exercise'),
    path('edit/<int:exercise_id>/', views.edit_exercise, name='edit_exercise'),
]
