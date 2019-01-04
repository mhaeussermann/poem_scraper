import requests
from bs4 import BeautifulSoup
import csv

setitems100 = "https://www.lyrikline.org/de/gedichte?listitems=100"
lyrikline_de = "https://www.lyrikline.org/de/gedichte?lang%5B%5D=de&seite="

# Iniate session with 100 items per page
s = requests.Session()
s.get(setitems100)

# Maximum pages
num_max = num

# Iterate through pages
for i in range(1, num_max):
    url = lyrikline_de + str(i)
    r = s.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Find respective element 
    results = soup.find("ul", class_="liste clearfix").findAll("li", recursive=False)
    lyrik_links = []
    #Get links to poems
    for result in results:  
        links = result.find('a', class_="row")
        lyrik_links.append(links.get('href'))
    lyrik_links = ["https://www.lyrikline.org" + x for x in lyrik_links]

print(lyrik_links)
