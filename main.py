from bs4 import BeautifulSoup
from html import unescape

with open('index.html') as f:
    raw = f.read()

soup = BeautifulSoup(raw, "html.parser")
cards = soup.select('#divwhite > div,#divblue > div,#divblack > div,#divred > div,#divgreen > div,#divmulticolored > div,#divcolorless > div,#divartifact > div,#divland > div')
for card in cards:
    img = card.select('p > img')
    img_url = img[0].get('src')
    name = img[0].get('alt')
    print('["' + img_url + '"' + ',' + '"' + name + '"],')
