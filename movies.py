import json


def read_movies_from_json():
    with open('movies.json', 'r') as file:
        data = json.load(file)
        return data['movies']


def get_movie_details(movie_id):
    movies = read_movies_from_json()
    for movie in movies:
        if movie['id'] == movie_id:
            return movie
    return None