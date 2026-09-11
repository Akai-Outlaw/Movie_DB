# Movie DB Dictionary Project
movie_db = {}

# Add a movie
def add_movie():
    title = input("Enter the movie title: ")
    year = input("Enter the movie year ")
    genre = input("Enter the movie genre: ")
    director = input("Enter the movie director: ")
    actors = input("Enter the actors (comma separted): ")

# Create movie in database
    movie_db[title] = {
        'year': year,
        'genre': genre,
        'director': director,
        'actors': actors.split(",")
    }

    print(f'{title} successfully added 🙌🏾')

# Edit a movie


# Delete a movie

# View all movies
def view_movies():
    print("Showing all movies 🍿")
    print("========================")
    for movie in movie_db:
        print(f"Movie: {movie_db}")
        for key, value in movie_db[movie].items():
            print(f"{key}: {value}")


# Search Movies

# Save and load movie from a title

# Error handling

# Data validation

while True:
    print('==== Movie Database MGT System ====')
    print("1. Quit")
    print("2. Add a movie")
    print("3. Show all movies")

    choice = input("What do you want to do? ")

    if choice == '1':
        print("See you later!! 👋🏾 ")
        break
    elif choice == '2':
        add_movie()
    elif choice == '3':
        view_movies()

    else:
        print("❌ Invalid Option. Try Again ")
