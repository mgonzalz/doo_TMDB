from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_results, name='search_results'),
    path('genres/', views.genre_list, name='genre_list'),
    path('genres/<str:genre>/', views.genre_detail, name='genre_detail'),

    path('movies/', views.movie_list, name='movie_list'),
    path('favorite-movie/<int:movie_id>/', views.toggle_favorite_movie, name='toggle_favorite_movie'),
    # Endpoints para Movies
    path('api/movies/', views.MovieListView.as_view(), name='movie-list-api'),
    path('api/movies/json', views.movie_list_json, name='movie-list-json'),

    path('tv-shows/', views.tv_show_list, name='tv_show_list'),
    path('favorite-tvshow/<int:tv_show_id>/', views.toggle_favorite_tvshow, name='toggle_favorite_tvshow'),
    # Endpoints para TVShows
    path('api/tv-shows/', views.TVShowListView.as_view(), name='tv-show-list-api'),
    path('api/tv-shows/json', views.tv_show_list_json, name='tv-show-list-json'),
]
