import requests
from bs4 import BeautifulSoup
import csv
import os

def scrapeData(url):
    
    try:

        response = requests.get(url)

        if(response.status_code == 200):
            print("Request Successful!")
        
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract Video Title
        title_tag = soup.find('meta', {'name': 'title'})
        title = title_tag['content'] if title_tag else 'No title found'

        # Extract Description
        description_tag = soup.find('meta', {'name': 'description'})
    
        description = description_tag['content'] if description_tag else 'No description found'

        # Extract View Count
        view_count_tag = soup.find('meta', itemprop='interactionCount')
        view_count = view_count_tag['content'] if view_count_tag else 'No view count found'
        
        # Extract Likes (Static scraping might not work due to dynamic content)
        # Find the button element with the specific class
        like_button = soup.find('button', class_='yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading yt-spec-button-shape-next--segmented-start')
        like_count = ""
        if like_button:
            # Extract the aria-label attribute
            aria_label = like_button.get('aria-label', '')
            # Extract the like count from the aria-label
            like_count = ''.join(filter(str.isdigit, aria_label.split(' ')[-2]))
            like_count = int(like_count.replace(',', ''))  # Convert to integer
            print(f'Like Count: {like_count}')
        else:
            print('Like button not found')
        
        # Define the data
        data = [
            ['Title', 'Description', 'View Count', 'Like Count'],  # Header
            [title, description, view_count, like_count]
        ]

        # Write data to CSV file
        filename = 'youtube_video_data.csv'
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print('Data saved to youtube_video_data.csv')
        

    except Exception as e:
        print(f"Failed to retrieve the webpage. Here is the error: {e}")


while True:
    url = input("Insert the url of the webpage you want to scrape here: ")
    answer = input("Is this the correct url?( yes/no): ")

    if("y" in answer):
        break

scrapeData(url)
