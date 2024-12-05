import pandas as pd
from movie_genre_scraper import Movie_Scraper

def recommend_random_movies(csv_file):
    try:
        df = pd.read_csv(csv_file)
        if df.empty:
            print("The CSV file is empty. Please make sure the file contains movie data.")
            return
        
        # Get 10 random movies
        recommendations = df.sample(n=10)
        
        print("\nRecommended Movies:")
        for index, row in recommendations.iterrows():
            print(f"Title: {row['title']}, Year: {row['year']}, Rating: {row['rating']}, Metascore: {row['metascore']}")
    
    except pd.errors.EmptyDataError:
        print("The CSV file is empty. Please make sure the file contains movie data.")
    except pd.errors.ParserError:
        print("There was a problem parsing the CSV file. Please check the file format.")

if __name__ == "__main__":
    # Run the scraper to get the movie data
    csv_file = Movie_Scraper()
    # Recommend random movies from the output CSV file
    recommend_random_movies(csv_file)
