# Poem scraper
Script to scrape the website Lyrikline for poems to create a corpus for research and experimentation. Up until this point, it just extracts the links for German poems and saves the respective poems to a .txt file. Hopefully, further versions will be more complex

## Usage
Run `scrape_poem_links.py` to create a link list using the variable, run `scrape_poems.py` to extract the text of the scraped links.

## Dependencies
The script requires [requests](https://pypi.org/project/requests2/) and [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) for scraping.