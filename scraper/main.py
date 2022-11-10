
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
        title = article.find('h2')
       
    except:
        print("Could not find puzzle text")

    file_name = title.text.replace('---', '').strip().replace(' ', '_')

    generate_readme(puzzle_text, file_name)



def generate_readme(puzzle, name):
    
    with open(f'{name}.md', 'a') as file:
            file.write(puzzle)
           




get_puzzle_text('https://adventofcode.com/2015/day/1')