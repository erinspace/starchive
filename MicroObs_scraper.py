## Scraper for MicroObs Image Directory!! ##

# http://mo-www.harvard.edu/ImageDirectory/Venus140607170650.FITS


## get a list of all the files on the MicroObs image directory right now

from bs4 import BeautifulSoup
import requests

url = requests.get('http://mo-www.harvard.edu/jsp/servlet/MO.ID.ImageDirectory')

text = url.text

soup = BeautifulSoup(text)

tag = soup.pre

# this is all the a tags in the pre tag 
tag.find_all('a')

# list of all the a tags in the pre tag
a_tags = list(soup.descendants)[2].find_all('a')

# this will print all the a tags that have the text we want
for item in tag.children:
    print list(item.next_sibling)[1]



print(soup.prettify())


# tag is the pre tag


# pre -> b -> first a

