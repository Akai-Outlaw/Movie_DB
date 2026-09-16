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
def edit_move():
    # Ask user what movie to edit
    title = input("Enter the movie title you want to update: ")

    try:
        
        # find move to edit
        if title not in movie_db:
                # if can't find movie keyerror
                raise KeyError(f"{title} not found in database")
        
            # Show current info
        print(f"Current information for {title}")
        print(movie_db[title])
        
        # Collect updated info from user
        year = input("Enter the movie year (or press Enter to keep current value(s)): ")
        genre = input("Enter the movie genre (or press Enter to keep current value(s)): ")
        director = input("Enter the movie director (or press Enter to keep current value(s)): ")
        actors = input("Enter the actors (comma separted) (or press Enter to keep current value(s)): ")

        
            # Update with new information 
        if year:
            movie_db[title]["year"] = year
        if genre:
            movie_db[title]["genre"] = genre
        if director:
            movie_db[title]["director"] = director
        if actors:
            movie_db[title]["actors"] = actors.split(",")

        print(f"{title} has been updated.")
    except Exception as e:
        print(f"❌ Error: {e}")


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

# Save Data - put db to file

# Load Data - pull previous database file into this program 
# We have to find a way, to repeatly ask the user what action they want to take
while True:
    print('==== 🎬 Movie Database MGMT System 🎬 ====')
    print('1. Exit')
    print('2. Add Movie')
    print('3. Show All Movies')
    print('4. Edit Existing Movie')
    print('5. Delete a Movie')
    print('6. Search for a Movie')
    print('7. Save data to a file')
    print('8. Load data from a file')

    choice = input('What do you want to do? ')

    if choice == '1':
        print('👋 Goodbye. Comeback soon!')
        break
    elif choice == '2':
        add_movie()
    elif choice == '3':
        view_movies()
    elif choice == '4':
        edit_move()
    elif choice == '5':
        print('Deleting a movie')
    elif choice == '6':
        print('Searching for movie')
    elif choice == '7':
        print('Saving data to file')
    elif choice == '8':
        print('Loading data from file')
    else:
        print('❌ Invalid Option. Please try again.')