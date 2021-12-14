from spider import *

# doc_link = "https://ieeexplore.ieee.org/document/8301529"
doc_link = "document/8301529"

papers = fetch_links(doc_link)

print('total papers:', len(papers))

for link in papers:
    print(link)
