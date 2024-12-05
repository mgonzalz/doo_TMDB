from django.db import models

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
