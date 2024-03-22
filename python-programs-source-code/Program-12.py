import requests
from bs4 import BeautifulSoup
import re

def scrape_bbc_news():
    # URL of the BBC News website
    url = "https://www.bbc.com/news"
    
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        news_links = soup.find_all('a')
        
        for link in news_links:
            title = link.text.strip()
            
            href = link.get('href')
            full_link = f"https://www.bbc.com{href}"
            
            print(f"Title: {title}")
            print(f"Link: {full_link}")
            print()
    else:
        print("Failed to retrieve data from the BBC News website.")

if __name__ == "__main__":
    scrape_bbc_news()
