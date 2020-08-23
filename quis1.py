from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd

alamat = 'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'
html = urlopen(alamat)
data = bs(html)

table = data.findAll('table', {'class':'wikitable'})[0]
rows = table.findAll('tr')

winner = []
for row in rows:
    content = row.select_one('b')
    if content:
        if '2019' in row.get_text():
            winner_data = []
            for data in row.findAll(['th','td']):
                winner_data.append(data.get_text().strip())
            winner.append(winner_data)

df_winner = pd.DataFrame(winner)
df_winner.columns = ['Film', 'Year', 'Awards', 'Nominations']
print(df_winner)