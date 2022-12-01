def create_urls():
    # adjust years to ranges needed if you want smaller range
    for year in range(2015, 2022):
        for day in range(1, 26):
            url = f'https://adventofcode.com/{year}/day/{day}'

            with open('urls.txt', 'a') as file:
                file.write(url)
                file.write('\n')

create_urls()