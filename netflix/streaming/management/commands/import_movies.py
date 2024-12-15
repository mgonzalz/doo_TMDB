from django.core.management.base import BaseCommand
from streaming.models import Movie
from streaming.utils import fetch_movies

class Command(BaseCommand):
    help = "Import movies from TMDB."

    def handle(self, *args, **kwargs):
        try:
            # Llama a la función para obtener las películas populares
            movies = fetch_movies()

            # Procesa cada película y guárdala en la base de datos
            for movie in movies:
                Movie.objects.update_or_create(
                    tmdb_id=movie['id'],
                    defaults={
                        'title': movie.get('title', 'Título desconocido'),
                        'description': movie.get('overview', ''),
                        'release_date': movie.get('release_date', None),
                        'genre': ', '.join(movie.get('genres', [])),
                        'vote_average': movie.get('vote_average', 0),
                        'poster_path': f"https://image.tmdb.org/t/p/w500{movie.get('poster_path', '')}",
                        'backdrop_path': f"https://image.tmdb.org/t/p/w500{movie.get('backdrop_path', '')}",
                    },
                )
            self.stdout.write(self.style.SUCCESS(f"Se importaron {len(movies)} películas populares correctamente."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error al importar películas populares: {e}"))
