# Description: This file contains the utility functions for the streaming app.

import requests

API_KEY = "d062936eba756bd8c896a4a6b1f795a4"
BASE_URL = "https://api.themoviedb.org/3"

def fetch_data_from_api(endpoint, params=None, language='es-ES'):
    if not params:
        params = {}

    url = f'{BASE_URL}/{endpoint}'
    params['api_key'] = API_KEY
    params['language'] = language
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error en la API: {response.status_code} - {response.text}")


def fetch_movies():
    """
    Obtiene una lista de películas populares desde el endpoint 'movie/popular' y traduce los géneros.
    """
    endpoint_genres = 'genre/movie/list'
    endpoint = 'movie/popular'
    genre_dict = {g['id']: g['name'] for g in fetch_data_from_api(endpoint_genres).get('genres', [])}
    response = fetch_data_from_api(endpoint)
    for movie in response.get('results', []):
        # Mapear géneros usando el diccionario
        movie['genres'] = [genre_dict.get(g_id, "Desconocido") for g_id in movie.get('genre_ids', [])]
    return response.get('results', [])


def fetch_tv_shows():
    """
    Obtiene una lista de series populares desde el endpoint 'tv/popular' sin paginación.
    """
    endpoint_genres = 'genre/tv/list'
    endpoint = 'tv/popular'
    genre_dict = {g['id']: g['name'] for g in fetch_data_from_api(endpoint_genres).get('genres', [])}
    response = fetch_data_from_api(endpoint)
    for tv_show in response.get('results', []):
        tv_show['genres'] = [genre_dict.get(g_id, "Desconocido") for g_id in tv_show.get('genre_ids', [])]
    return response.get('results', [])
