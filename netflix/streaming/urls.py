from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('tv-shows/', views.tv_show_list, name='tv_show_list'),
]
