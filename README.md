# Netflix: The Movie Database.
Este proyecto es una aplicación desarrollada en Django que imita algunas funcionalidades básicas de la popular plataforma de streaming Netflix. Los usuarios pueden crear cuentas, buscar películas y series, añadir o quitar títulos de su lista personal ("Mi Lista") y explorar contenidos actualizados periódicamente mediante web scraping automatizado.

**Tecnologías Implementadas:**
- **Docker**: Infraestructura Contenerizada
- **Github Actions**: Automatización
- **Figma**: Diseño UI/UX
- **PostgreSQL**: Bases de Datos.
- **Vercel**: Despliegue en la Nube.

## Repositorio.
- Link: https://github.com/mgonzalz/doo_tmdb.git
- Usuario: María González - [@mgonzalz](https://github.com/mgonzalz)
- Despliegue en Vercel: [https://doo-tmdb.vercel.app/](https://doo-tmdb.vercel.app/)

## Caraterísticas.
### Front-End.
En este caso, el diseño de la interfaz de usuario se ha inspirado en un prototipo creado en **Figma**. Se ha tomado como referencia la maqueta del proyecto [_MOVIE WEBSITE UI DESIGN_](https://www.figma.com/design/ARHPXdX8x3HlKJ1V7GV2il/MOVIE-WEBSITE-UI-DESIGN?node-id=0-1&t=Z7tVJ1fYANWjeOz9-1), lo cual permitió construir una interfaz similar a la de plataformas de streaming modernas.

- **HTML y CSS**: Implementados para estructurar y estilizar la presentación de la aplicación, garantizando una interfaz de usuario intuitiva y agradable.
- **Django Templates**: Utilizados para la generación dinámica de contenido en las páginas web, permitiendo que los datos de películas y series se integren de manera fluida en el diseño.

### Back-End.
- **Django Framework**: Motor principal de la aplicación.
- **Django ORM**: Manejo de datos en la base de datos.
- **The Movie Database API (TMDb)**: Fuente principal de datos para películas y series

### Bases de datos.
- **PostgreSQL** para producción: La base de datos utilizada en producción es PostgreSQL, una solución robusta y escalable.
- **SQLite** para desarrollo: Durante el desarrollo local, se utiliza SQLite para facilitar la configuración.

### Automatización.
**Actualización de contenido**: Se ha configurado un workflow en ***GitHub Actions*** que, cada mes, ejecuta un proceso automatizado de web scraping para obtener datos actualizados sobre películas y series desde The Movie Database (TMDb). Esto garantiza que la aplicación esté al día con los nuevos lanzamientos y actualizaciones.

## Estructura del Proyecto.
```python
netflix
├── netflix/               # Carpeta principal de la aplicación
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── authentication/        # Aplicación para manejar autenticación y usuarios
├── streaming/             # Aplicación para manejar películas y series
├── media/
│   # Configuración de Docker para ejecutar el proyecto localmente.
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```
## Instalación.

### Creación de un Entorno Virtual.

Primero, crea un entorno virtual llamado `env-django`:

```bash
python -m venv env-django
env-django\Scripts\activate
```

- Nota: Si usas **VSCode**, puedes necesitar configurar permisos antes de activar el entorno: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`

Una vez que el entorno virtual esté activado, instala las dependencias:

```bash
pip install -r requirements.txt
```

### Configuración de Docker.

Si se prefiere ejecutar el proyecto en local con Docker, puede consultar el archivo `DockerSetUp.md` para una guía detallada sobre cómo configurar y ejecutar el proyecto usando Docker.

### Migración de la Base de Datos y Ejecución del Servidor.

Para aplicar las migraciones y ejecutar el servidor de desarrollo, usa los siguientes comandos:

```bash
cd netflix
python manage.py migrate
python manage.py runserver
```

Una vez hecho esto, abre tu navegador y accede a **http://127.0.0.1:8000/** para ver la página de inicio. Para acceder al panel de administración de Django, ve a **http://127.0.0.1:8000/admin** e ingresa con las credenciales del superusuario.

## Despliegue en Vercel.

El proyecto está configurado para desplegarse automáticamente en **Vercel**. Cualquier cambio realizado en el repositorio se despliega automáticamente a través de la integración con Vercel. Puedes ver el sitio en producción en [https://doo-tmdb.vercel.app/](https://doo-tmdb.vercel.app/).
