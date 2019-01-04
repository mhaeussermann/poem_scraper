import requests
from bs4 import BeautifulSoup
import pickle

# import poem url list
with open ('poem_links.csv', 'rb') as fp:
    lyrik_links = pickle.load(fp)

# Testfall
test = lyrik_links[3]
print(test)
# loop through items in list

# scrape urls from poem url list
r = requests.get(test)
soup = BeautifulSoup(r.content, 'html.parser')
# extract author (h1 id="gedicht-autor")
author = soup.find(id='gedicht-autor')
p_author = author.text
# extract title (h3 class="gedicht-origtitel-header")
title = soup.find(class_='gedicht-origtitel-header')
p_title = title.text
# extract text of poem (div class="gedicht-originaltext clearfix ")
poem_text = soup.find(class_='gedicht-originaltext clearfix')
p_text = poem_text.text

print(p_author)
print(p_title)
print(p_text)

# conc author, title and text and save as file