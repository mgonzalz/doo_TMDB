from django.shortcuts import render
from .models import *
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "streaming/movie_list.html", {"movies": movies})

def tv_show_list(request):
    tv_shows = TVShow.objects.all()
    return render(request, "streaming/tv_show_list.html", {"tv_shows": tv_shows})
