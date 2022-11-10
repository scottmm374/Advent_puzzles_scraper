#!/usr/bin/python

from bs4 import BeautifulSoup
from urllib.error import URLError
import requests



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
        print(puzzle_text)
       
    except:
        print("Could not find puzzle text")


get_puzzle_text('https://adventofcode.com/2015/day/1')