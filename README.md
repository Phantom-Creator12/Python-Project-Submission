# Python-Project-Submission
**README
Movie Scraper and Recommendation System**
This project consists of two main scripts: movie_genre_scraper.py and Recommender.py
These scripts work together to scrape movie data from IMDb and provide random movie recommendations based on the data.

**Prerequisites**
Before running the scripts, ensure you have the following Python packages installed:
• requests
• beautifulsoup4
• pandas

Can be installed using pip:
_pip install requests beautifulsoup4 pandas

**Scripts Overview**
**1. movie_genre_scraper.py**
This script scrapes movie data from IMDb based on user inputs for genre, start year, minimum IMDb rating, and minimum metascore. The data is saved to a CSV file.
**2. Recommender.py**
This script imports the Movie_Scraper function from scrape_movies.py, uses the generated CSV file, and recommends 10 random movies from that file.

**Usage**
**Scraping Movie Data**
1. Run the scrape_movies.py script:
_        python movie_genre_scraper.py
2. Follow the prompts to enter:
  • Movie genre (e.g., action, comedy, drama)
  • Start year (e.g., 2000)
  • Minimum IMDb rating (e.g., 7.0)
  • Minimum Metascore (e.g., 50)
3. The script will fetch the top 250 movies (or fewer if criteria are not met) that match the specified criteria and save the data to a CSV file named after the genre.


**Recommending Random Movies**
1. Run the Recommender.py script
2. The script will automatically call the Movie_Scraper function to generate the CSV file and then recommend 10 random movies from the data.

   
**Example**
Here's an example of how to use the scripts:

1. Run the Recommender.py script
2. Enter the following inputs when prompted:
  • Genre: action
  • Start Year: 2000
  • Minimum IMDb Rating: 7.0
  • Minimum Metascore: 50
3. The script will save the data to action_top_250_movies.csv
4. The script will read the action_top_250_movies.csv file and print the details of 10 random movies from the list.

   
**Error Handling**
**Scrape Movies Script**
• If an invalid genre is entered (non-alphabetic characters), the script will prompt you to enter a valid genre.
• If an invalid year is entered (non-4-digit year), the script will prompt you to enter a valid 4-digit year.
• If an invalid rating or metascore is entered (non-numeric values), the script will prompt you to enter valid numeric values.

**Recommend Movies Script**
• If the CSV file is empty or improperly formatted, the script will print an error message and guide you to check the file.
