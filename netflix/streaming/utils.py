# Description: This file contains the utility functions for the streaming app.

import requests

API_KEY = "d062936eba756bd8c896a4a6b1f795a4"
BASE_URL = "https://api.themoviedb.org/3"

def fetch_movies():
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&language=en-US&sort_by=popularity.desc"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    return []
