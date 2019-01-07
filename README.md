# Poem scraper
Script that can be used to search and scrape the website Lyrikline for poems to create a text corpus for academic research and experimentation. Up until this point, it just extracts links to German poems and saves their text to a .txt file. Hopefully, further versions will allow for more complex search operations.

## Usage
Run `scrape_poem_links.py` to create a link list using the variable, run `scrape_poems.py` to extract the text of the scraped links.

## Dependencies
The script requires [requests](https://pypi.org/project/requests2/) and [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) for scraping.