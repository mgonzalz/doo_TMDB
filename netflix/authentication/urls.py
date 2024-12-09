from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.UserProfileView.as_view(), name='user-profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout_view, name='logout'),
]
