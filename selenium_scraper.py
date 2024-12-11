from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
import pandas as pd
import re

def Movie_Scraper():
    def get_genre_movies(genre, start_year, min_rating, min_metascore):
        """
        Fetches the top movies in a given genre from IMDb starting from a specific year
        with minimum rating, vote count, and metascore criteria.

        Args:
        genre (str): The genre of movies to fetch.
        start_year (int): The starting year for movie release date.
        min_rating (float): The minimum IMDb rating for the movies.
        min_metascore (int): The minimum metascore for the movies.

        Returns:
        list: A list of dictionaries containing movie details.
        """
        print(f"Fetching information for the top 250 movies in the {genre} genre from the year {start_year} onwards...")

        # Initialize the WebDriver using the Service class
        service = Service('C:/path/to/chromedriver.exe')
        driver = webdriver.Chrome(service=service)

        # Construct the URL for the IMDb search page based on the provided genre, start year, and vote count
        url = f"https://www.imdb.com/search/title/?genres={genre}&sort=user_rating,desc&count=250&start_year={start_year}&num_votes=2500,"
        driver.get(url)

        movies = []
        try:
            # Wait for the movie list to load
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'lister-item')))

            items = driver.find_elements(By.CLASS_NAME, 'lister-item')
            print(f"Number of movies found: {len(items)}")  # Debugging output

            for item in items:
                try:
                    # Extract the movie title
                    title = item.find_element(By.CLASS_NAME, 'lister-item-header').find_element(By.TAG_NAME, 'a').text.strip()
                    print(f"Title: {title}")  # Debugging output
                    # Extract the release year
                    year = item.find_element(By.CLASS_NAME, 'lister-item-year').text.strip()
                    print(f"Year: {year}")  # Debugging output
                    # Extract the IMDb rating
                    rating_tag = item.find_element(By.CLASS_NAME, 'ratings-imdb-rating').find_element(By.TAG_NAME, 'strong')
                    rating = rating_tag.text.strip() if rating_tag else 'N/A'
                    print(f"Rating: {rating}")  # Debugging output
                    # Extract the metascore
                    metascore_tag = item.find_elements(By.CLASS_NAME, 'metascore')
                    metascore = int(metascore_tag[0].text.strip()) if metascore_tag else 0
                    print(f"Metascore: {metascore}")  # Debugging output

                    # Filter movies based on rating and metascore criteria
                    if rating != 'N/A' and float(rating) >= min_rating and metascore >= min_metascore:
                        movies.append({
                            'title': title,
                            'year': year,
                            'rating': rating,
                            'metascore': metascore
                        })
                except Exception as e:
                    print(f"Error processing item: {e}")

        except TimeoutException:
            print("Timed out waiting for page to load")
        finally:
            driver.quit()

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
        if not movies:
            print("No movies found matching the criteria.")
            return None

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
    save_to_csv(movies, genre)

if __name__ == "__main__":
    Movie_Scraper()
