from spider import *

doc_link = "https://ieeexplore.ieee.org/document/8301529"

papers = fetch_links(doc_link)

for link in papers:
    print(link)
