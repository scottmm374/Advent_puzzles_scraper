#!/usr/bin/python
import os
import time
from pathlib import Path
from urllib.error import URLError
import requests
from bs4 import BeautifulSoup
from env import HEADERS

def main():

    with open('urls.txt', 'r') as file:
         for url in file:
             time.sleep(10)
             puzzle_url = url.strip()
             input_url = f'{puzzle_url}/input'
            
    
             puzzle_text, file_name, year = get_puzzle_text(puzzle_url)
             input_text = get_input(input_url)
             create_directories(puzzle_text, file_name, year, input_text)


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

    return(puzzle_text, file_name, year)



def get_input(url):
    # using urls and my session token to pull puzzle input data to write to txt files

    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()

    except URLError:
            print("The Server Could Not be Found")

    soup = BeautifulSoup(response.content, "html.parser")
    return soup


def create_directories(puzzle, title, year, input_text):

        # Creates all the directories, sub-directories, .py, .txt and .md with puzzle instructions
        main_dir = "Advent"
        os.makedirs(main_dir, exist_ok=True)

        # Creates directories by year
        directory = str(year)
        os.makedirs(os.path.join(main_dir, directory), exist_ok=True)
        
        # Create Sub-directories
        sub_dir = f'{title}'

        os.makedirs(os.path.join(main_dir, directory, sub_dir), exist_ok=True)
        os.makedirs(os.path.join(main_dir, directory, sub_dir), exist_ok=True)
            
        # Creates .md with Puzzle instructions
        with open(os.path.join(main_dir,directory, sub_dir, f'{title}.md'), "w" ) as file:
                file.write(puzzle)

        # Creates .py file for each sub directory
        Path(os.path.join(main_dir, directory, sub_dir,  "main.py")).touch()

        # Creates .txt file with puzzle inputs
        with open(os.path.join(main_dir, directory, sub_dir, "input.txt"), 'w') as i_file:
                i_file.writelines(str(input_text))


if __name__=="__main__":
    main()
