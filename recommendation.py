import movies

def get_movie_suggestions(genre):
    movies_data = movies.read_movies_from_json()
    suggestions = []
    for movie in movies_data:
        if movie['genre'].lower() == genre.lower():
            suggestions.append(movie)
    return suggestions