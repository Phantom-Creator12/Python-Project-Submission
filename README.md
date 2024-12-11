# Python-Project-Submission
# Movie Recommendation System

This project provides a basic movie recommendation system using the TMDB API. 

**How to Use:**

**Prerequisites**
Before running the scripts, ensure you have the following Python packages installed:  
• requests  
• time  
• pandas   
• urlencode   
• random  

Can be installed using pip:  
_pip install requests pandas time urlencode random  

*****Scripts Overview***

**1. tmdb_scraper.py**  
    - Scrapes movie data from the TMDB API based on user input (genre, minimum rating, minimum vote count, etc.).   
    - Saves the scraped data to a CSV file with the genre name.   
**2. tmdb_recommender.py**    
    - Reads the saved CSV file containing movie data for a given genre.    
    - Recommends a random selection of 10 movies from the dataset.    
    - Displays the recommended movies with their titles, release years, ratings, and vote counts.   

**Usage**  
**Scraping Movie Data** ( Can be run as a standalone file to scrape and save data in csv file)  
1. Run the tmdb_scraper.py script:  

2. Follow the prompts to enter:  
  • Enter your API key : (Prompt to enter your API key) :  
  • Movie genre (a list of genre is shown e.g., action, comedy, drama) :    
  • Start year (e.g., 2000) :  
  • Minimum rating (e.g., 7.0) :   
  • Minimum votevount for the ratings (e.g., 1000) :    
3. The script will fetch all the results based on search criteria, and save the data to a CSV file named after the genre.  


**Recommending Random Movies**
1. Run the tmdb_recommender.py script
2. The script will automatically call the Movie_Scraper function from tmdb_scraper.py script
3. Follow the prompts to enter:
  • Enter your API key : 
  • Enter the genre: 
  • Enter the release date start year (e.g., 2000): 
  • Enter the minimum rating (e.g., 7.0): 
  • Enter the minimum vote count (e.g., 500): 
4. After the file is saved, function reads the csv file and gives 10 random moive names with release year, ratings and vote_count.

   
**Example**
Here's an example of how to use the scripts:  

1. Run the tmdb_recommender.py script  
2. Enter the following inputs when prompted:   
  • Enter your API key : xxxxxxxxxxxxxxxxxxx     
  • Enter the genre: action   
  • Enter the release date start year (e.g., 2000): 2000   
  • Enter the minimum rating (e.g., 7.0): 7.0   
  • Enter the minimum vote count (e.g., 500): 500   
4. The script will save the data to tmdb_movies_genre.csv
5. The script will read the tmdb_movies_genre.csv file and print the details of 10 random movies from the list.  

   
**Error Handling**
**Scrape Movies Script**   
• If an invalid genre is entered (non-alphabetic characters), the script will prompt you to enter a valid genre.    
• If an invalid year is entered (non-4-digit year), the script will prompt you to enter a valid 4-digit year.   
• If an invalid rating is entered (non-numeric values), the script will prompt you to enter valid numeric values.   
• If an invalid vote_count is entered (non-numeric values), the script will prompt you to enter valid numeric values.   


**Recommend Movies Script**
• If the CSV file is empty or improperly formatted, the script will print an error message and guide you to check the file.   
