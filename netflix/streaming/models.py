from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model): # Info: https://developer.themoviedb.org/reference/discover-movie
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    genre = models.TextField(max_length=100, blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)
    poster_path = models.URLField(blank=True, null=True)
    backdrop_path = models.URLField(blank=True, null=True)
    tmdb_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.title


class TVShow(models.Model): # Info: https://developer.themoviedb.org/reference/discover-tv
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    genre = models.TextField(max_length=100, blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)
    poster_path = models.URLField(blank=True, null=True)
    backdrop_path = models.URLField(blank=True, null=True)
    tmdb_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True, related_name='favorited_by')
    tv_show = models.ForeignKey(TVShow, on_delete=models.CASCADE, blank=True, null=True, related_name='favorited_by')

    def __str__(self):
        if self.movie:
            return f"{self.user.username} - {self.movie.title}"
        if self.tv_show:
            return f"{self.user.username} - {self.tv_show.title}"
