import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def Movie_Scraper():
    def get_genre_movies(genre, start_year, min_rating, min_metascore):

        print(f"Fetching information for the top 250 movies in the {genre} genre from the year {start_year} onwards...")

        # Construct the URL for the IMDb search page based on the provided genre, start year, and vote count
        url = f"https://www.imdb.com/search/title/?release_date={start_year},&num_votes=2500,&genres={genre}&count=250&sort=user_rating,desc"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        movies = []
        for item in soup.find_all('div', class_='.ipc-metadata-list.ipc-metadata-list--dividers-between.sc-748571c8-0.gFCVNT.detailed-list-view.ipc-metadata-list--base'):
            # Extract the movie title
            title = item.h3.find('.ipc-title__text').text.strip()
            # Extract the release year
            year = item.h3.find('span', class_='.sc-300a8231-7 eaXxft dli-title-metadata-item').text.strip()
            # Extract the IMDB rating
            rating_tag = item.find('span', class_='.ipc-rating-star--rating').strong.text.strip()
            rating = rating_tag.strong.text.strip() if rating_tag else 'N/A'
            # Extract the metascore
            metascore_tag = item.find('span', class_='sc-b0901df4-0 bXIOoL metacritic-score-box')
            metascore = int(metascore_tag.text.strip()) if metascore_tag else 0
            
            # Filter movies based on rating and metascore criteria
            if rating != 'N/A' and float(rating) >= min_rating and metascore >= min_metascore:
                movies.append({
                    'title': title,
                    'year': year,
                    'rating': rating,
                    'metascore': metascore
                })

        return movies

    def get_valid_genre():
        """
        Prompts the user to enter a valid movie genre and returns it.
        """
        while True:
            genre = input("Enter the genre: ").strip()
            if re.match("^[a-zA-Z]+$", genre):
                return genre.lower()
            else:
                print("Invalid genre. Please enter a genre using only alphabetic characters.")

    def get_valid_year():
        """
        Prompts the user to enter a valid start year for movie release date and returns it.
        """
        while True:
            year = input("Enter the release date start year (e.g., 2000): ").strip()
            if re.match(r"^\d{4}$", year):
                return year
            else:
                print("Invalid year. Please enter a valid 4-digit year.")

    def get_valid_metascore():
        """
        Prompts the user to enter a valid minimum metascore and returns it.
        """
        while True:
            metascore = input("Enter the minimum metascore (e.g., 50): ").strip()
            try:
                metascore = float(metascore)
                return metascore
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_valid_rating():
        """
        Prompts the user to enter a valid minimum IMDb rating and returns it.
        """
        while True:
            rating = input("Enter the minimum rating (e.g., 7.0): ").strip()
            try:
                rating = float(rating)
                return rating
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def save_to_csv(movies, genre):
        """
        Saves the list of movies to a CSV file named after the genre.
        """
        df = pd.DataFrame(movies)
        filename = f"{genre}_top_250_movies.csv"
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
        return filename

    # Get user inputs for genre, start year, minimum metascore, and minimum rating
    genre = get_valid_genre()
    start_year = get_valid_year()
    min_metascore = get_valid_metascore()
    min_rating = get_valid_rating()

    # Fetch the movie data and save it to a CSV file
    movies = get_genre_movies(genre, start_year, min_rating, min_metascore)
    return save_to_csv(movies, genre)

if __name__ == "__main__":
    Movie_Scraper()




