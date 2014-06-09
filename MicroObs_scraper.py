## Scraper for MicroObs Image Directory!! ##

from bs4 import BeautifulSoup
import requests

url = requests.get('http://mo-www.harvard.edu/jsp/servlet/MO.ID.ImageDirectory')

text = url.text

soup = BeautifulSoup(text)

# everything is contained in the <pre> tag
tag = soup.pre

# This finds all the tags with the text in them we want
all_a = [b.find('a', text=True) for b in tag.findAll('b')]

file_names = []

for filename in all_a:
    file_names.append(filename.text)

file_names = [ext.replace('GIF','FITS') for ext in file_names]

print file_names
print file_names

base_url = 'http://mo-www.harvard.edu/ImageDirectory/'

for filename in file_names[1:3]:
    filename = filename.strip()
    FITs_file = requests.get(base_url + filename)
    with open(filename, "wb") as newfile:
        newfile.write(FITs_file.content)
