#Movie Recommender

import pandas as pd
import random
import tmdb_scraper as ts  # Ensure this is your module name and correct import

def recommender(csv_filename):
    try:
        df = pd.read_csv(csv_filename)
        
        if df.empty or len(df) < 10:
            print("Not enough movies to suggest.")
            return
        
        random_movies = df.sample(n=10)
        
        print("Here are 10 random movie suggestions for you:")
        for index, row in random_movies.iterrows():
            print(f"Title: {row['title']}, Year: {row['year']}, Rating: {row['rating']}, Vote Count: {row['vote_count']}")
    
    except FileNotFoundError:
        print(f"Error: File {csv_filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Take API key as input from the user
    API_KEY = input("Enter your TMDB API key: ")
    
    # Take genre input from the user
    genre, genre_id = ts.get_valid_genre()
    
    # Run the Movie_Scraper to generate the CSV file
    ts.Movie_Scraper(API_KEY, genre, genre_id)

    # Use the genre to determine the filename
    csv_filename = f"tmdb_movies_{genre}.csv"

    # Recommend 10 random movies from the CSV file
    recommender(csv_filename)
