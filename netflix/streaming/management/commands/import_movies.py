from django.core.management.base import BaseCommand
from streaming.models import Movie
from streaming.utils import fetch_movies

class Command(BaseCommand):
    help = "Import movies from TMDB"

    def handle(self, *args, **kwargs):
        movies = fetch_movies()
        for movie in movies:
            Movie.objects.update_or_create(
                tmdb_id=movie['id'],
                defaults={
                    'title': movie['title'],
                    'description': movie.get('overview', ''),
                    'release_date': movie.get('release_date', None),
                    'genre': ', '.join([str(genre_id) for genre_id in movie.get('genre_ids', [])]),
                    'vote_average': movie.get('vote_average', None),
                    'poster_path': f"https://image.tmdb.org/t/p/w500{movie.get('poster_path', '')}",
                    'backdrop_path': f"https://image.tmdb.org/t/p/w500{movie.get('backdrop_path', '')}",
                },
            )
        self.stdout.write(self.style.SUCCESS("Movies imported successfully!"))
