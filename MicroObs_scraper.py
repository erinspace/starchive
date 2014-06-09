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
    file_names.append(filename.text)

file_names = [ext.replace('GIF','FITS') for ext in file_names]

print file_names


# request url = http://mo-www.harvard.edu/ImageDirectory/CentaurusA140609034607.FITS
