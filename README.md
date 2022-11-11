# Advent_puzzles_scraper


Web scraper and directory/file generator to save previously released Advent of Code puzzles in a single location.


[Visit Advent of Code](https://adventofcode.com)

# Table of Contents
- [Why did I create this project?](https://github.com/scottmm374/Advent_puzzles_scraper#motivation)
- [Features](https://github.com/scottmm374/Advent_puzzles_scraper#features)
- [Tech used](https://github.com/scottmm374/Advent_puzzles_scraper#techframework)
- [Screenshots](https://github.com/scottmm374/Advent_puzzles_scraper#screenshots)
- [Future features](https://github.com/scottmm374/Advent_puzzles_scraper#roadmap)
- [What is Advent of Code anyway?](https://github.com/scottmm374/Advent_puzzles_scraper#what-is-advent-of-code) 


# Motivation   
<em>TLDR</em> - Im lazy, and repetitive, boring tasks make me want to pull my hair out

I'm a programmer... We are supposed to automate absolutely everything, right? :)

![Alt text](images/download.jpeg)

I discovered [Advent of Code](https://adventofcode.com) in late 2019 while I was a student at Bloomtech (Lambda when I attended).
While the current year puzzles open up to solve on their corresponding date, all previous puzzles are available on the website to solve.

I wanted a way to save the puzzle instructions, puzzle input, and solve all the puzzles in ONE location.
Each year there are 25 puzzles, and 25 bonus puzzles. Thats 300 Puzzles previously released! 

Could you imagine how long trying to copy paste would take, way to long!

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

If you haven't yet, you should REALLY check it out!