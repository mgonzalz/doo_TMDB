from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
    path('', views.movie_list, name='movie_list'),
]
