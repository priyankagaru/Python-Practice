import re
import requests
from bs4 import BeautifulSoup as bs

URL='https://en.wikipedia.org/wiki/India'
r=requests.get(URL)
soup=bs(r.text,'html.parser')
images_body=soup.find('div',attrs={'id':'content','class':'mw-body'})
#image_div=images_body.find_all('div',attrs={'class':'thumbimage'})
#image_source=images_body.find_all('img')
#print(image_source.text)
for image in images_body.find_all('img'):
    print(image['src'], '\n')

print('\n\n')   

