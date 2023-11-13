#To download all the draw results from 2007 to now for Euromillions, 
# you can use Python's `requests` and `BeautifulSoup` libraries. Here is a sample script that you can use:

#```python
import requests
import requests
from bs4 import BeautifulSoup
import csv

# URL of the archive page
url = "https://www.euro-millions.com/results-history-?as=TXT&year="
#https://www.euro-millions.com/results-history-2004

# Destination folder to download the results to
folder_path = r"C:\Users\johnc\OneDrive\Documents\Python\Tkinter\euromillions_archive"

# Create a file in the above folder called euromillions_result.csv
file_path = folder_path + r"\euromillions_result.csv"
with open(file_path, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Date", "Numbers", "Stars"])

    # Loop through all years from 2007 to current year
    for year in range(2004, 2024):
        # Get the HTML content of the archive page for the current year
        response = requests.get(url + str(year))
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the draw results from the HTML content
        draws = soup.find_all('tr', {'class': 'draw'})

        # Write the draw results to the CSV file
        for draw in draws:
            date = draw.find('td', {'class': 'date'}).text.strip()
            numbers = draw.find('td', {'class': 'numbers'}).text.strip().replace(' ', ',')
            stars = draw.find('td', {'class': 'stars'}).text.strip().replace(' ', ',')
            writer.writerow([date, numbers, stars])

print("All draw results have been downloaded to " + file_path)

#This script will download all the draw results from 2007 to the current year and save them to a CSV file named `euromillions_result.csv` in the folder `C:\Users\johnc\OneDrive\Documents\Python\Tkinter\euromillions_archive`. The CSV file will have three columns: `Date`, `Numbers`, and `Stars`. Each row will represent a single draw result.

#Please note that the script assumes that the destination folder already exists. If the folder does not exist, the script will raise an error. You may need to modify the script to create the folder if it does not exist.


# Source: Conversation with Bing, 13/11/2023
# (1) GitHub - pawisoon/euroScraper: Python script for scraping the newest .... https://github.com/pawisoon/euroScraper.
# (2) pyeuromil · PyPI. https://pypi.org/project/pyeuromil/.
# (3) GitHub - guillempp/Euromillions: Python script to check if you won on .... https://github.com/guillempp/Euromillions.
# (4) GitHub - pedro-mealha/euromillions-api: Nano API to fetch Euromillions .... https://github.com/pedro-mealha/euromillions-api.
# (5) GitHub - acpirience/pyeuromil: A python library to check and analyse .... https://github.com/acpirience/pyeuromil.
# (6) undefined. https://www.euro-millions.com/results-archive-2005.
# (7) undefined. https://www.kaggle.com/pawisoon/datasets.
# (8) undefined. https://euromillions.api.pedromealha.dev.
# (9) undefined. https://euromillions.staging.api.pedromealha.dev.
# (10) undefined. https://www.euro-millions.com.
# (11) euromillions · GitHub Topics · GitHub. https://github.com/topics/euromillions.
# (12) Getty Images. https://www.gettyimages.com/detail/news-photo/in-this-photo-illustration-a-pen-and-a-scratch-card-on-news-photo/1228538256.