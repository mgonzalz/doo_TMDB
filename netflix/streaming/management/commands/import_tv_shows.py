from django.core.management.base import BaseCommand
from streaming.models import TVShow
from streaming.utils import fetch_tv_shows
from datetime import datetime

class Command(BaseCommand):
    help = "Import TV Shows from TMDB."

    def handle(self, *args, **kwargs):
        try:
            # Llama a la función para obtener todas las series populares
            tv_shows = fetch_tv_shows()

            # Procesa cada serie y guárdala en la base de datos
            for show in tv_shows:
                # Obtener y limpiar la fecha de lanzamiento
                release_date = show.get('first_air_date', None)

                # Validar y manejar posibles valores no válidos
                if release_date and release_date.strip():  # Si no está vacío o en blanco
                    try:
                        release_date = datetime.strptime(release_date.strip(), '%Y-%m-%d').date()
                    except ValueError:
                        self.stderr.write(
                            self.style.WARNING(
                                f"Fecha no válida para la serie {show.get('name', 'Título desconocido')}: {release_date}"
                            )
                        )
                        release_date = None
                else:
                    release_date = None

                # Guardar o actualizar la serie en la base de datos
                TVShow.objects.update_or_create(
                    tmdb_id=show['id'],
                    defaults={
                        'title': show.get('name', 'Título desconocido'),
                        'description': show.get('overview', ''),
                        'release_date': release_date,
                        'genre': ', '.join(show.get('genres', [])),
                        'vote_average': show.get('vote_average', 0),
                        'poster_path': f"https://image.tmdb.org/t/p/w500{show.get('poster_path', '')}",
                        'backdrop_path': f"https://image.tmdb.org/t/p/w500{show.get('backdrop_path', '')}",
                    },
                )

            self.stdout.write(self.style.SUCCESS(f"Se importaron {len(tv_shows)} series populares correctamente."))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error al importar series populares: {e}"))
