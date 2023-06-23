import movies
import recommendation

def show_menu():
    while True:
        print("==== Movie Recommendation System ====")
        print("1. Get movie details")
        print("2. Get movie suggestions")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            movie_id = int(input("Enter the movie ID: "))
            movie = movies.get_movie_details(movie_id)
            if movie:
                print(f"Title: {movie['title']}")
                print(f"Genre: {movie['genre']}")
            else:
                print("Movie not found!")
        elif choice == '2':
            genre = input("Enter your preferred genre: ")
            suggestions = recommendation.get_movie_suggestions(genre)
            if suggestions:
                print("Movie Suggestions:")
                for movie in suggestions:
                    print(f"Title: {movie['title']}")
                    print(f"Genre: {movie['genre']}")
                    print("---")
            else:
                print("No suggestions available!")
        elif choice == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == '__main__':
    show_menu()