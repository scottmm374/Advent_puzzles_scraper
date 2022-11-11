
import os
import time
from pathlib import Path
from urllib.error import URLError
import requests
from bs4 import BeautifulSoup



def get_puzzle_text(url):
    # Scraper using bs4
    try:
        response = requests.get(url, allow_redirects=False)
        response.raise_for_status()

    except URLError:
            print("The Server Could Not be Found")

    soup = BeautifulSoup(response.content, "html.parser")
    
    
    try:
        article = soup.find('article', attrs={'class': 'day-desc'})
        puzzle_text = article.prettify()
        title = article.find('h2')
       
    except:
        print("Could not find puzzle text")

    try:
        # extracting year for directory names
        nav = soup.find('nav')
        anchor = nav.a
        year = str(anchor).replace('<a href="/', '').replace('/about">[About]</a>', '')
        
    except:
        print("couldnt find year")
    
    #  Puzzle titles Used for subfolder and md  file naming 
    file_name = title.text.replace('---', '').strip().replace(' ', '_')

    create_directories(puzzle_text, file_name, year)


def get_url():
    #  Function to read and feed each puzzle url to scrape 
 
    with open('urls.txt', 'r') as file:
        for url in file:
            time.sleep(10)
            get_puzzle_text(url.strip())


def create_directories(puzzle, title, year):
    # Creates all the directories, sub-directories, .py, .txt and .md with puzzle instructions
    
        # Creates directories by year
        directory = str(year)
        os.makedirs(directory, exist_ok=True)
        
        # Create Sub-directories
        sub_dir = f'{title}'

        os.makedirs(os.path.join(directory, sub_dir), exist_ok=True)
        os.makedirs(os.path.join(directory, sub_dir), exist_ok=True)
            
        # Creates .md with Puzzle instructions
        with open(os.path.join(directory, sub_dir, f'{title}.md'), "w" ) as file:
                file.write(puzzle)
        # Creates txt and py file for each sub directory
        Path(os.path.join(directory, sub_dir, "input.txt")).touch()
        Path(os.path.join(directory, sub_dir,  "main.py")).touch()


get_url()
