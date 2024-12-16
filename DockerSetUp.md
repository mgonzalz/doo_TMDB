# Configuración de Docker para el Proyecto Django.
Este archivo explica cómo configurar y ejecutar el proyecto Django utilizando Docker. Asegúrate de seguir estos pasos para correr el proyecto en un contenedor Docker de manera eficiente.

Se debe de tener instalado lo siguiente:
- [Docker](https://www.docker.com/get-started) (incluyendo Docker Compose)
- [WSL](https://learn.microsoft.com/es-es/windows/wsl/install) (a través del comando `wsl --install`)

Los archivos del Docker se deberán de guardar en la raíz del proyecto. Deben de existir los siguientes:
- Docker Compose: `docker-compose.yml` es un archivo de configuración que define cómo se deben configurar y ejecutar los contenedores dentro de Docker. Este archivo permite **gestionar múltiples contenedores**, como aplicaciones, bases de datos o servicios secundarios, sin necesidad de ejecutar comandos individuales para cada uno.
- Dockerfile: El `Dockerfile` es un archivo de texto que contiene una serie de instrucciones para construir una imagen Docker. Define cómo se debe configurar el entorno dentro de un contenedor para ejecutar tu aplicación. A partir de este archivo, Docker construye una imagen, que luego puedes usar para crear un contenedor. Es fundamental, indica al Docker **qué hacer paso a paso** para construir una imagen que pueda ejecutar tu aplicación, instalar dependencias, configurar variables de entorno y más.
- DockerIgnore: El archivo `.dockerignore` le indica a Docker qué **archivos o directorios no deben incluirse al construir una imagen Docker**. Esto es útil para evitar que archivos innecesarios se copien dentro de la imagen, lo que reduce el tamaño de la imagen y mejora la eficiencia.

## Construcción de la imagen del Docker.
Para construir la imagen Docker desde el archivo `Dockerfile`, ejecuta el siguiente comando en la raíz del proyecto:

```bash
docker-compose build
```
Esto descargará la imagen base de Python y instalará todas las dependencias necesarias especificadas en el `requirements.txt`.

## Ejecución de los Contenedores.
Una vez que la imagen haya sido construida, puedes ejecutar los contenedores con Docker Compose:

```bash
docker-compose up
```
Cuando se ejecuta un contenedor de Docker con Django y se muestra en la consola `http://0.0.0.0:8080/`, esta dirección solo es válida dentro del contenedor. La dirección `0.0.0.0` le indica al servidor que escuche en todas las interfaces de red dentro del contenedor, pero **no es accesible desde fuera del contenedor**, es decir, no se puede acceder a través del navegador. Para acceder a la aplicación desde tu navegador en la máquina local, debes usar `http://localhost:8080/` o `http://127.0.0.1:8080/`.
