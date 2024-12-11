from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import pandas as pd
import re

def Movie_Scraper():
    def get_genre_movies(genre, start_year, min_rating, min_metascore):
        print(f"Fetching information for the top 250 movies in the {genre} genre from the year {start_year} onwards...")

        service = Service(r'C:\Users\abhi1\.vscode\chromedriver-win64\chromedriver.exe')
        driver = webdriver.Chrome(service=service)

        url = f"https://www.imdb.com/search/title/?title_type=feature&release_date={start_year},&user_rating={min_rating},10&num_votes=2500,&genres={genre}&count=250&sort=user_rating,desc"
        driver.get(url)

        movies = []
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'lister-item')))
            
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            items = soup.find_all('div', class_='lister-item')
            print(f"Number of movies found: {len(items)}")

            for item in items:
                try:
                    # Extract the movie title
                    title = item.h3.a.text.strip()
                    print(f"Title: {title}")
                    # Extract the release year
                    year = item.h3.find('span', class_='lister-item-year').text.strip()
                    print(f"Year: {year}")
                    # Extract the IMDb rating
                    rating_tag = item.find('div', class_='ratings-imdb-rating').strong
                    rating = rating_tag.text.strip() if rating_tag else 'N/A'
                    print(f"Rating: {rating}")
                    # Extract the metascore
                    metascore_tag = item.find('span', class_='metascore')
                    metascore = int(metascore_tag.text.strip()) if metascore_tag else 0
                    print(f"Metascore: {metascore}")

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
        while True:
            genre = input("Enter the genre: ").strip()
            if re.match("^[a-zA-Z]+$", genre):
                return genre.lower()
            else:
                print("Invalid genre. Please enter a genre using only alphabetic characters.")

    def get_valid_year():
        while True:
            year = input("Enter the release date start year (e.g., 2000): ").strip()
            if re.match(r"^\d{4}$", year):
                return year
            else:
                print("Invalid year. Please enter a valid 4-digit year.")

    def get_valid_metascore():
        while True:
            metascore = input("Enter the minimum metascore (e.g., 50): ").strip()
            try:
                metascore = float(metascore)
                return metascore
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_valid_rating():
        while True:
            rating = input("Enter the minimum rating (e.g., 7.0): ").strip()
            try:
                rating = float(rating)
                return rating
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def save_to_csv(movies, genre):
        if not movies:
            print("No movies found matching the criteria.")
            return None

        df = pd.DataFrame(movies)
        filename = f"{genre}_top_250_movies.csv"
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
        return filename

    genre = get_valid_genre()
    start_year = get_valid_year()
    min_metascore = get_valid_metascore()
    min_rating = get_valid_rating()

    movies = get_genre_movies(genre, start_year, min_rating, min_metascore)
    save_to_csv(movies, genre)

if __name__ == "__main__":
    Movie_Scraper()
