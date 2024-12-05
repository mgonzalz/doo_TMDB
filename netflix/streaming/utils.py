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
    Obtiene una lista de películas populares desde el endpoint 'movie/popular'.
    """
    endpoint = 'movie/popular'
    response = fetch_data_from_api(endpoint)
    return response.get('results', [])

def fetch_tv_shows():
    """
    Obtiene una lista de series populares desde el endpoint 'tv/popular' sin paginación.
    """
    endpoint = 'tv/popular'
    response = fetch_data_from_api(endpoint)
    return response.get('results', [])
