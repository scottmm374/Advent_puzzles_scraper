# Advent_puzzles_scraper


Web scraper and directory/file generator to save previously released Advent of Code puzzles in a single location.


[Visit Advent of Code](https://adventofcode.com)

# Table of Contents
- Why did I create this project?
- Features
- Tech used
- Screenshots
- Future features
- What is [Advent of Code](https://adventofcode.com) anyway? 


# Motivation   
<em>TLDR</em> - Im lazy, and repetitive tasks make me want to pull my hair out

I'm a programmer... We are supposed to automate absolutely everything, right? :)


I discovered Advent of Code in late 2019 while I was still a student at Lambda (a.k.a. Bloomtech).
While the current year puzzles open up to solve on their corresponding date, all previous puzzles are available on the website to solve.

Each year there are 25 puzzles, as well as 25 bonus puzzles for a total of 50. Thats a lot of puzzles to create a folder, and all the files, so I decided to automate it!

I wanted a way to organize all the puzzles by the year in ONE location, my repo :)
Could you imagine how long trying to copy paste would take, way to long!

I started solving puzzles in repelit but quickly realized I wanted solve them and keep them in a central location, (Github repository).

I also wanted a better way to process the input given for each puzzle.

<em>If you haven't seen the input on some of these, they are VERY long!</em>

So I created .txt files to store the input, to be read and processed however I needed in my functions to solve the puzzles.



# Features


- Creates directories labeled by year for previous puzzles available on Advent of Code (2015-202)
- Creates sub directories labeled by puzzle title inside each year directory. (25)
- Creates .txt file for puzzle input (optional)
- Creates .md file with Puzzle instructions scraped from website.
- Creates a .py file (For solving) :) 

# Screenshots
</table>
<br>

<table width='100%' align='center'>
<tr>
<td><img src='images/year_directories.png'></td>
<td><img src='images/puzzle_file.png'  ></td>

</tr>
<tr>
<td><img src='images/puzzle_sub_directories.png' ></td>
<td><img src='images/puzzle_readme.png'></td>
</tr>
<!-- <td><img src='images/puzzle_file.png' ></td> -->

</tr>
</table>



# Tech/Framework

- [Python3](https://www.python.org/downloads/)
- [beautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [requests](https://pypi.org/project/requests/)
- [urllib](https://docs.python.org/3/library/urllib.html)
- [pathlib](https://docs.python.org/3/library/pathlib.html)
- [os](https://docs.python.org/3/library/os.html)

# Roadmap

- Add ability to scrape input and part 2 puzzles, that require OAuth login.
- Add the ability to scrape new released puzzles into their directories on each day they are released.


### What is Advent of Code?

[Advent of Code](https://adventofcode.com)

Advent of code is a website created by Eric Wastl in 2015.

Every year on December 1st a new puzzle is released each day until December 25th.

These puzzles can be solved in any programming language and any skill level can play.
