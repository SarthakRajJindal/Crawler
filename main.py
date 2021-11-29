from spider import *

max_articles = 10

doc_link = "https://ieeexplore.ieee.org/document/8301529"

x = fetch_links(doc_link)

for y in x:
    print(y)
