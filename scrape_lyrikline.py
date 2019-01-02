import requests
from bs4 import BeautifulSoup

lyrikline_de = "https://www.lyrikline.org/de/gedichte?query=&lang%5B%5D=de&listitems=100"

page = requests.get(lyrikline_de, timeout=5)
soup = BeautifulSoup(page.content, 'html.parser')

#for page_number in range(1,10):
    
    # To form the url based on page numbers
#    url = lyrikline_de+"&page="+str(page_number)
#    r = requests.get(url)
#    soup = BeautifulSoup(r.content, "html.parser")

# To extract the results
#lyrik_list = soup.find_all("ul", class_="liste clearfix")
#lyrik_list_items = lyrik_list.find_all("li")
#lyrik_list_links = soup.find_all('a', class_="row")

results = soup.find("ul", { "class" : "liste clearfix" }).findAll("li", recursive=False)

lyrik_links = []  
for result in results:  
    links = result.find('a', { "class" : "row" })
    print links.get('href')
    #lyrik_links.append(links)

#print(type(lyrik_links))