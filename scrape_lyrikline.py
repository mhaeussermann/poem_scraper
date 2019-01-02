import requests
from bs4 import BeautifulSoup
import datetime
import csv

#end_page_num = 26

lyrikline_de = "https://www.lyrikline.org/de/gedichte?query=&lang%5B%5D=de&listitems=100&page="

page = requests.get(lyrikline_de)
soup = BeautifulSoup(page.content, 'html.parser')

#Get links to Lyrics
results = soup.find("ul", class_="liste clearfix").findAll("li", recursive=False)
lyrik_links = []  
for result in results:  
    links = result.find('a', class_="row")
    lyrik_links.append(links.get('href'))
lyrik_links = ["https://www.lyrikline.org" + x for x in lyrik_links]

print(lyrik_links)
