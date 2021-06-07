import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL='https://en.wikipedia.org/wiki/Johnny_Depp_filmography'
response=requests.get(URL)
soup=bs(response.text,'html.parser')
filmography={
    "year":[],
    'title':[],
    'roles':[],
    'notes':[],
    'ref':[],
}

table_body=soup.find('table',attrs={'class':'wikitable'}).find('tbody').find_all('tr')
#table_data=table_body.find('tr')[1]
#print(table_data.text)
for row in table_body[1:]:
    cells1=row.find_all('th')
    cells=row.find_all('td')
    filmography['year'].append(cells1[0].text.strip())
    filmography['title'].append(cells[0].text.strip())
    filmography['roles'].append(cells[1].text.strip())
    filmography['notes'].append(cells[2].text.strip())
    filmography['ref'].append(cells[3].text.strip())

df=pd.DataFrame(filmography)
print(df.to_string())
