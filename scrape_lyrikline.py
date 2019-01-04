import requests
from bs4 import BeautifulSoup
import datetime
import csv

lyrikline_de = "https://www.lyrikline.org/de/gedichte?query=&lang%5B%5D=de&listitems=100&page="

page = requests.get(lyrikline_de)
soup = BeautifulSoup(page.content, 'html.parser')

# Iterate through pages
def get_next_page_link(soup):
    lis = soup.select('li.pager')
    if lis:
        return lis[0].find('a')
    return None

# Get links to Lyrpoemsics
results = soup.find("ul", class_="liste clearfix").findAll("li", recursive=False)
lyrik_links = []  
for result in results:  
    links = result.find('a', class_="row")
    lyrik_links.append(links.get('href'))
lyrik_links = ["https://www.lyrikline.org" + x for x in lyrik_links]

print(lyrik_links)
