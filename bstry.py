import requests
from bs4 import BeautifulSoup
import csv
   
# URL = "http://www.values.com/inspirational-quotes"
URL = "https://ieeexplore.ieee.org/document/738001/"

r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html.parser')

# print(soup.prettify())

title = soup.find("meta", property="og:title")
abstract = soup.find("meta", property="twitter:description")

print(title["content"] if title else "No meta title given")
print(abstract["content"] if url else "No meta url given")