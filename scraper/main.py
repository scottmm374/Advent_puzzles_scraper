
from bs4 import BeautifulSoup
from urllib.error import URLError
import os
from pathlib import Path
import requests
import time



def get_puzzle_text(url):

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

    file_name = title.text.replace('---', '').strip().replace(' ', '_')

    create_directories(puzzle_text, file_name, year)


def get_url():
    start = time.time()
    time.sleep(15)
    end = time.time()
    print(f"Time elapsed, url {(end - start):.5f} seconds")

    with open('urls.txt', 'r') as file:
        for url in file:
            get_puzzle_text(url.strip())


def create_directories(puzzle, title, year):
    
        directory = str(year)
        os.makedirs(directory, exist_ok=True)
        
        sub_dir = f'{title}'

        # Creates directories

        os.makedirs(os.path.join(directory, sub_dir), exist_ok=True)
        os.makedirs(os.path.join(directory, sub_dir), exist_ok=True)
            
        # Readme with Puzzle instructions
        with open(os.path.join(directory, sub_dir, f'{title}.md'), "w" ) as file:
                file.write(puzzle)

        Path(os.path.join(directory, sub_dir, "input.txt")).touch()
        Path(os.path.join(directory, sub_dir,  "main.py")).touch()
    



get_puzzle_text('https://adventofcode.com/2015/day/1')

# get_url()