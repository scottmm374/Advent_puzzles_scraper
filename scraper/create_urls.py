def create_urls():
    # adjust years to ranges needed if you want smaller range
    for year in range(2022, 2023):
        for day in range(2, 3):
            url = f'https://adventofcode.com/{year}/day/{day}'

            with open('urls.txt', 'a') as file:
                file.write(url)
                file.write('\n')

create_urls()