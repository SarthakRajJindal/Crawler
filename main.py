from spider import *

max_articles = 10

x = fetch_links('https://ieeexplore.ieee.org/document/8301529/references')

for y in x:
    print(y)
