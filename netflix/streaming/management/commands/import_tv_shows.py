from django.core.management.base import BaseCommand
from streaming.models import TVShow
from streaming.utils import fetch_tv_shows

class Command(BaseCommand):
    help = "Importa las series populares desde TMDb y las guarda en la base de datos."

    def handle(self, *args, **kwargs):
        try:
            # Llama a la función para obtener todas las series populares
            tv_shows = fetch_tv_shows()

            # Procesa cada serie y guárdala en la base de datos
            for show in tv_shows:
                TVShow.objects.update_or_create(
                    tmdb_id=show['id'],
                    defaults={
                        'title': show.get('name', 'Título desconocido'),
                        'description': show.get('overview', ''),
                        'release_date': show.get('first_air_date', None),
                        'genre': ', '.join(map(str, show.get('genre_ids', []))),
                        'vote_average': show.get('vote_average', 0),
                        'poster_path': f"https://image.tmdb.org/t/p/w500{show.get('poster_path', '')}",
                        'backdrop_path': f"https://image.tmdb.org/t/p/w500{show.get('backdrop_path', '')}",
                    },
                )
            self.stdout.write(self.style.SUCCESS(f"Se importaron {len(tv_shows)} series populares correctamente."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error al importar series populares: {e}"))
