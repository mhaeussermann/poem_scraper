import requests
from bs4 import BeautifulSoup
import pickle
import os
import re

# import poem url list
with open ('poem_links.csv', 'rb') as fp:
    lyrik_links = pickle.load(fp)

# prepare folder for poems
d = os.path.dirname(os.path.abspath(__file__)) # directory of script
d2 = d + '/poems/' # path to be created

try:
    os.makedirs(d2)
except OSError:
    pass

# testing the script with a limited number of links
#lyrik_links = lyrik_links[500:]
#print(test)

# loop through items in list
for i in range(0, len(lyrik_links), 1):
# scrape urls from poem url list
    print("Extracting poem - " + str(i+1) + "/" + str(len(lyrik_links)))
    r = requests.get(lyrik_links[i])
    soup = BeautifulSoup(r.content, 'html.parser')
# extract author (h1 id="gedicht-autor")
    author = soup.find(id='gedicht-autor')
    p_author = author.text
    #print(p_author)
# extract title (h3 class="gedicht-origtitel-header")
    title = soup.find(class_='gedicht-origtitel-header')
    p_title = title.text
    p_clean_title = re.sub('[^a-zA-Z0-9 \n\.]', '', p_title)
    #print(p_title)
# extract text of poem (div class="gedicht-originaltext clearfix ")
    poem_text = soup.find(class_='gedicht-originaltext clearfix')
    for br in poem_text.find_all("br"):
        br.replace_with("\n" + br.text)
    p_text = poem_text.text
    #print(p_text)

    file_name = d2 + p_author + ' - ' + p_clean_title + '.txt'
    if not os.path.exists(file_name):
    # name file as 'author - title' and save poem text in file
        with open(file_name, 'w') as f:
            f.write(p_text.encode("UTF-8"))
            print("Poem saved!")
    else:
        print("The file already exists!")