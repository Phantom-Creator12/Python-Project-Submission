# File: tmdb_scraper.py

import requests
import pandas as pd
import re
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def get_valid_genre():
    """
    Prompts the user to enter a valid movie genre and returns its TMDB genre ID.
    """
    genres = {
        'action': 28,
        'adventure': 12,
        'animation': 16,
        'comedy': 35,
        'crime': 80,
        'documentary': 99,
        'drama': 18,
        'family': 10751,
        'fantasy': 14,
        'history': 36,
        'horror': 27,
        'music': 10402,
        'mystery': 9648,
        'romance': 10749,
        'science fiction': 878,
        'tv movie': 10770,
        'thriller': 53,
        'war': 10752,
        'western': 37
    }

    print("Available genres: ", ", ".join(genres.keys()))

    while True:
        genre = input("Enter the genre: ").strip().lower()
        if genre in genres:
            return genre, genres[genre]
        else:
            print("Invalid genre. Please enter a valid genre from the list.")

def Movie_Scraper(api_key, genre, genre_id):
    def get_genre_movies(genre, genre_id, start_year, min_rating, min_vote_count, pages=5):
        """
        Fetches the top movies in a given genre from TMDB starting from a specific year
        with minimum rating and vote count criteria.

        Args:
        genre (str): The name of the genre.
        genre_id (int): The ID of the genre of movies to fetch.
        start_year (int): The starting year for movie release date.
        min_rating (float): The minimum TMDB rating for the movies.
        min_vote_count (int): The minimum vote count for the movies.
        pages (int): Number of pages to fetch from the API.

        Returns:
        list: A list of dictionaries containing movie details.
        """
        print(f"Fetching information for the top movies in the {genre} genre from the year {start_year} onwards...")

        movies = []
        for page in range(1, pages + 1):
            url = (f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}&primary_release_date.gte={start_year}-01-01"
                   f"&vote_average.gte={min_rating}&vote_count.gte={min_vote_count}&sort_by=vote_average.desc&page={page}")

            session = requests.Session()
            retry = Retry(connect=5, backoff_factor=0.5)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)

            response = session.get(url)
            if response.status_code != 200:
                print(f"Failed to fetch data: {response.status_code}")
                break

            movies_data = response.json().get('results', [])
            if not movies_data:
                break

            for item in movies_data:
                try:
                    title = item.get('title', 'N/A')
                    year = item.get('release_date', 'N/A').split('-')[0]
                    rating = item.get('vote_average', 'N/A')
                    vote_count = item.get('vote_count', 0)

                    if rating != 'N/A' and float(rating) >= min_rating and vote_count >= min_vote_count:
                        movies.append({
                            'title': title,
                            'year': year,
                            'rating': rating,
                            'vote_count': vote_count
                        })
                except Exception as e:
                    print(f"Error processing item: {e}")

            print(f"Page {page}: Number of movies found: {len(movies_data)}")

        return movies

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

    def get_valid_rating():
        """
        Prompts the user to enter a valid minimum TMDB rating and returns it.
        """
        while True:
            rating = input("Enter the minimum rating (e.g., 7.0): ").strip()
            try:
                rating = float(rating)
                return rating
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_valid_vote_count():
        """
        Prompts the user to enter a valid minimum vote count and returns it.
        """
        while True:
            vote_count = input("Enter the minimum vote count (e.g., 500): ").strip()
            try:
                vote_count = int(vote_count)
                return vote_count
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def save_to_csv(movies, genre):
        """
        Saves the list of movies to a CSV file named after the genre.
        """
        if not movies:
            print("No movies found matching the criteria.")
            return None

        df = pd.DataFrame(movies)
        df.to_csv(f'tmdb_movies_{genre}.csv', index=False)
        print(f"Data saved to tmdb_movies_{genre}.csv")
        
    start_year = get_valid_year()
    min_rating = get_valid_rating()
    min_vote_count = get_valid_vote_count()

    movies = get_genre_movies(genre, genre_id, start_year, min_rating, min_vote_count)
    save_to_csv(movies, genre)

if __name__ == "__main__":
    API_KEY = input("Enter your TMDB API key: ")  # Take API key as input from user
    genre, genre_id = get_valid_genre()
    Movie_Scraper(API_KEY, genre, genre_id)
