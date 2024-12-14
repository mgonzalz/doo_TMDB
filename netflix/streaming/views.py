from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .utils import *
from django.contrib.auth.decorators import login_required
import random
# Create your views here.

## Vista basada a través de plantillas.
def home(request):
    # Obtener todas las películas y series
    movies = Movie.objects.all()
    tv_shows = TVShow.objects.all()
    combined_items = list(movies) + list(tv_shows)
    random.shuffle(combined_items)

    # Top 10 películas y series con mejor calificación
    top_movies = movies.order_by('-vote_average')[:10]
    top_tvshows = tv_shows.order_by('-vote_average')[:10]
    top_combined = sorted(
        list(top_movies) + list(top_tvshows),
        key=lambda x: x.vote_average,
        reverse=True
    )[:10]

    # Novedades combinadas (últimas películas y series)
    new_movies = movies.order_by('-release_date')[:10]
    new_tvshows = tv_shows.order_by('-release_date')[:10]
    new_combined = sorted(
        list(new_movies) + list(new_tvshows),
        key=lambda x: x.release_date or "",
        reverse=True
    )[:10]

    # Mi Lista (Películas y Series)
    my_list = []
    favorite_ids = []
    if request.user.is_authenticated:
        favorite_movie_ids = Playlist.objects.filter(user=request.user, movie__isnull=False).values_list('movie_id', flat=True)
        favorite_tvshow_ids = Playlist.objects.filter(user=request.user, tv_show__isnull=False).values_list('tv_show_id', flat=True)
        favorite_ids = list(favorite_movie_ids) + list(favorite_tvshow_ids)

        my_list = list(movies.filter(id__in=favorite_movie_ids)) + list(tv_shows.filter(id__in=favorite_tvshow_ids))

    return render(request, 'streaming/home.html', {
        'items': combined_items,
        'top_combined': top_combined,
        'new_combined': new_combined,
        'my_list': my_list,
        'favorite_ids': favorite_ids,
    })


def movie_list(request):
    movies = Movie.objects.all()
    favorite_movie_ids = []
    # Top 10 películas con mejor calificación
    top_movies = Movie.objects.order_by('-vote_average')[:10]
    # Últimas 10 películas basadas en la fecha de lanzamiento
    new_movies = Movie.objects.order_by('-release_date')[:10]
    if request.user.is_authenticated:
        favorite_movie_ids = Playlist.objects.filter(user=request.user, movie__isnull=False).values_list('movie_id', flat=True)
    
    return render(request, 'streaming/movie_list.html', {
        'movies': movies,
        'favorite_movie_ids': favorite_movie_ids,
        'top_movies': top_movies,
        'new_movies': new_movies,
    })
def tv_show_list(request):
    tv_shows = TVShow.objects.all()
    favorite_tvshow_ids = []
    # Top 10 series con mejor calificación
    top_tvshows = TVShow.objects.order_by('-vote_average')[:10]
    # Últimas 10 series basadas en la fecha de lanzamiento
    new_tvshows = TVShow.objects.order_by('-release_date')[:10]

    if request.user.is_authenticated:
        favorite_tvshow_ids = Playlist.objects.filter(user=request.user, tv_show__isnull=False).values_list('tv_show_id', flat=True)
    
    return render(request, 'streaming/tv_show_list.html', {
        'tv_shows': tv_shows,
        'favorite_tvshow_ids': favorite_tvshow_ids,
        'top_tvshows': top_tvshows,
        'new_tvshows': new_tvshows,
    })

# Endpoints para agregar o eliminar de favoritos.
@login_required
def toggle_favorite_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    favorite, created = Playlist.objects.get_or_create(user=request.user, movie=movie)
    if not created:
        favorite.delete()  # Eliminar de favoritos si ya estaba en la lista
    return redirect('movie_list')


@login_required
def toggle_favorite_tvshow(request, tv_show_id):
    tv_show = TVShow.objects.get(id=tv_show_id)
    favorite, created = Playlist.objects.get_or_create(user=request.user, tv_show=tv_show)
    if not created:
        favorite.delete()  # Eliminar de favoritos si ya estaba en la lista
    return redirect('tv_show_list')

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


## Vista basada a través de JSON.
def movie_list_json(request):
    try:
        data = fetch_movies()
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def tv_show_list_json(request):
    try:
        data = fetch_tv_shows()
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
