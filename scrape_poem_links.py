import requests
from bs4 import BeautifulSoup
import pickle

setitems100 = "https://www.lyrikline.org/de/gedichte?listitems=100"
lyrikline_de = "https://www.lyrikline.org/de/gedichte?lang%5B%5D=de&seite="

# Iniate session with 100 items per page
s = requests.Session()
s.get(setitems100)

# Maximum pages
num_max = # Add how many pages you want to scrape: 1 page includes 100 items

# Empty list for the links
lyrik_links = []

# Iterate through pages
for i in range(1, num_max):
    url = lyrikline_de + str(i)
    r = s.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Find respective element 
    results = soup.find('ul', class_='liste clearfix').findAll('li', recursive=False)
    #Get links to poems
    for result in results:  
        links = result.find('a', class_='row')
        lyrik_links.append(links.get('href'))

# Add lyrikline url to the scraped links
lyrik_links = ['https://www.lyrikline.org' + x for x in lyrik_links]

# Test print
#print(lyrik_links)
print(len(lyrik_links))

# Export the poem url list as a text file
with open('poem_links.csv', 'wb') as fp:
    pickle.dump(lyrik_links, fp)