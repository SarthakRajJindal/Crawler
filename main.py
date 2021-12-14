from spider import *
import requests
from bs4 import BeautifulSoup
import csv

# doc_link = "https://ieeexplore.ieee.org/document/8301529"
doc_link = "/document/8301529"

papers = fetch_links(doc_link)

print('total papers:', len(papers))

field_names= ['No', 'doc_link', 'title', 'abstract']
list_papers = []
cnt = 0

for link in papers:
    print(link)
    URL = "https://ieeexplore.ieee.org" + link

    r = requests.get(URL)
    
    soup = BeautifulSoup(r.content, 'html.parser')

    # print(soup.prettify())

    title = soup.find("meta", property="og:title")
    abstract = soup.find("meta", property="twitter:description")

    cnt = cnt + 1
    dic = {'No' : cnt, 'doc_link' : link, 'title' : title["content"] , 'abstract' : abstract["content"] }
    list_papers.append(dic)

    # print(title["content"] if title else "No meta title given")
    # print(abstract["content"] if url else "No meta url given")
    # print('------------------------------------------------------\n')

with open('papers.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(list_papers)

print('Done!')