from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
import csv

alamat = 'https://pokemondb.net/pokedex/all'
req = Request(alamat, headers={'User-Agent' : 'Mozilla/5.0'})
html = urlopen(req)
data = bs(html, 'html.parser')

table = data.find('table', {'id' : 'pokedex'})
rows = table.findAll('tr', limit=29)

pokes = []
for row in rows:
    poke_datas = []
    for data in row.findAll(['th','td']):
        poke_data = data.get_text()
        poke_datas.append(poke_data)
    pokes.append(poke_datas)

with open('pokedesk.csv', "w+", newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    for row in pokes:
        writer.writerow(row)
