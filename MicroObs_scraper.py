## Scraper for MicroObs Image Directory!! ##

from bs4 import BeautifulSoup
import requests

url = requests.get('http://mo-www.harvard.edu/jsp/servlet/MO.ID.ImageDirectory')

text = url.text

soup = BeautifulSoup(text)

tag = soup.pre

# this is all the a tags in the pre tag 
tag.find_all('a')

# This finds all the tags with the text in them we want
all_a = [b.find('a', text=True) for b in tag.findAll('b')]

file_names = []

for filename in all_a:
    file_names.add(filename.text)

print file_names


# print(soup.prettify())


# tag is the pre tag


# pre -> b -> first a

# anchors = [td.find('a') for td in soup.findAll('td')]

# That should find the first "a" inside each "td" in the html you provide. 
# You can tweak td.find to be more specific or else use findAll if 
# you have several links inside each td.

