from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
import pandas as pd

alamat = 'https://pokemondb.net/pokedex/all'
req = Request(alamat, headers={'User-Agent' : 'Mozilla/5.0'})
html = urlopen(req)
data = bs(html, 'html.parser')

table = data.find('table', {'id' : 'pokedex'})
rows = table.findAll('tr', limit=17)

pokes = []
for row in rows:
    poke_datas = []
    for data in row.findAll(['th','td']):
        poke_data = data.get_text().strip()
        poke_datas.append(poke_data)
    pokes.append(poke_datas)

df_pokes = pd.DataFrame(pokes)
df_pokes_head = df_pokes.iloc[0]
df_pokes.columns = df_pokes_head
df_pokes = df_pokes[1:]
df_pokes.reset_index(drop=True)

df_pokes.to_excel('TugasPythonLanjutan_Hari_10_Hanif_Yuli_Abdillah_P.xlsx', sheet_name='pokemon_data', index=False)