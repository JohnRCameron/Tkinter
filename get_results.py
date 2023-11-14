#To download all the draw results from 2007 to now for Euromillions, 
# you can use Python's `requests` and `BeautifulSoup` libraries. Here is a sample script that you can use:

#```python
import requests
import requests
from bs4 import BeautifulSoup
import csv

# URL of the archive page
# "https://www.lottology.com/europe/euromillions/past-draws-archive/?as=XLS&year="

url = "https://lottohub.co.uk/results/euromillions/draw-history-"

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