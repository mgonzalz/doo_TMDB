from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
# Create your views here.

## Vista basada a través de plantillas.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "streaming/movie_list.html", {"movies": movies})

def tv_show_list(request):
    tv_shows = TVShow.objects.all()
    return render(request, "streaming/tv_show_list.html", {"tv_shows": tv_shows})


## Vista basada a través de API Rest - obtiene un JSON.
class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

class TVShowListView(APIView):
    def get(self, request):
        tv_shows = TVShow.objects.all()
        serializer = TVShowSerializer(tv_shows, many=True)
        return Response(serializer.data)
