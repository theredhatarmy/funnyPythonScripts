import requests
from bs4 import BeautifulSoup
import threading
import time
import os

# Create a directory for saving the results if it doesn't exist
if not os.path.exists('scraped_data'):
    os.mkdir('scraped_data')

# Function to download a web page
def download_page(url):
    try:
        print(f"Downloading {url}...")
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None

# Function to extract the title from the page content
def extract_title(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    title = soup.find('title')
    return title.text if title else "No title found"

# Function to save the extracted title to a file
def save_title(url, title):
    file_name = os.path.join('scraped_data', f"{url.replace('https://', '').replace('http://', '').replace('/', '_')}_title.txt")
    with open(file_name, 'w') as file:
        file.write(f"URL: {url}\n")
        file.write(f"Title: {title}\n")
    print(f"Saved title for {url} to {file_name}")

# Function to process a list of URLs (scrape and save the data)
def process_url(url):
    page_content = download_page(url)
    if page_content:
        title = extract_title(page_content)
        save_title(url, title)

# List of URLs to scrape
urls = [
    'https://www.example.com',
    'https://www.wikipedia.org',
    'https://www.github.com',
    'https://www.python.org'
]

# Create a thread for each URL and start them concurrently
threads = []
start_time = time.time()
for url in urls:
    thread = threading.Thread(target=process_url, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

end_time = time.time()
print(f"Scraping completed in {end_time - start_time:.2f} seconds.")
