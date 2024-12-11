
# IMDb Movie Scraper

This script scrapes movie data from IMDb using Selenium and BeautifulSoup. It allows users to specify the genre, starting year, minimum rating, and minimum Metascore to filter the results.

**Features:**    

- **Web Scraping:** Uses Selenium to interact with the IMDb website and extract data.  
- **Data Extraction:** Extracts movie titles, release years, IMDb ratings, and Metascores using BeautifulSoup.   
- **Data Filtering:** Filters movies based on user-defined criteria (genre, starting year, minimum rating, and minimum Metascore).   
- **Data Saving:** Saves the scraped data to a CSV file.   

**Requirements:**  

- Python   
- Selenium   
- pandas  

**Installation:**

pip install selenium pandas

**Before Running:**

**Download ChromeDriver:**
Download the appropriate ChromeDriver executable for your operating system and browser from the official ChromeDriver website (https://chromedriver.chromium.org/).
Replace 'C:/path/to/chromedriver.exe' in the code with the actual path to your downloaded ChromeDriver executable.

**How to Run:**
Execute the tmdb_scraper.py script.  
Enter the required information when prompted:    
 Genre    
 Starting year    
 Minimum rating  
 Minimum Metascore  
The script will scrape the data and save it to a CSV file with the name [genre]_top_250_movies.csv.

**Note:**
This script requires a valid ChromeDriver executable to function correctly.  
The script may be subject to changes in IMDb's website structure, which could break the scraping logic.  
Always use web scraping responsibly and adhere to the website's terms of service.  
This script is for educational purposes only and should not be used for malicious activities.  
