from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    # Endpoints para Movies
    path('api/movies/', views.MovieListView.as_view(), name='movie-list'),
    path('api/movies/json', views.movie_list_json, name='movie_list'),

    path('tv-shows/', views.tv_show_list, name='tv_show_list'),
    # Endpoints para TVShows
    path('api/tv-shows/', views.TVShowListView.as_view(), name='tv-show-list'),
    path('api/tv-shows/json', views.tv_show_list_json, name='tv_show_list'),
]
