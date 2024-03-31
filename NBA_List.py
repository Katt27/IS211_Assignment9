import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_NBA_champions"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})
data = []
headers = [header.text.strip() for header in table.find_all('th')]

for row in table.find_all('tr'):
    cols = row.find_all('td')
    if len(cols) > 0:
        row_data = {}
        for i, val in enumerate(cols):
            row_data[headers[i]] = val.text.strip()
        data.append(row_data)

df_nba = pd.DataFrame(data)
print(df_nba)

#df_nba.to_csv('nba_champions.csv', index=False)
