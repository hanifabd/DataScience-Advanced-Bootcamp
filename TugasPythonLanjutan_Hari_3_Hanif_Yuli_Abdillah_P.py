from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd

def soal1():
    alamat = 'https://en.wikipedia.org/wiki/List_of_brightest_stars'
    html = urlopen(alamat)
    data = bs(html)

    table = data.findAll('table', {'class':'wikitable'})[0]
    rows = table.findAll('tr')

    df = []
    for row in rows:
        aRow = []
        for cell in row.findAll(['th','td']):
            data = cell.get_text()
            aRow.append(data.strip())
        df.append(aRow)

    df = pd.DataFrame(df)
    head = df.iloc[0]
    df.columns = head
    df = df[1:]
    df.reset_index(drop=True)

    df['Spectral class'].iloc[0] = df['Distance (ly)'].iloc[0]
    df['Distance (ly)'].iloc[0] = df['part 2'].iloc[0]
    df['part 2'].iloc[0] = ''

    return df

def soal2():
    alamat = 'https://en.wikipedia.org/wiki/List_of_action_films_of_the_2020s'
    html = urlopen(alamat)
    data = bs(html)

    tables = data.findAll('table', {'class':'wikitable'})[0:2]

    i = 0
    list_movie = []
    for table in tables:
        rows = tables[i].findAll('tr')
        for row in rows:
            aRow = []
            for cell in row.findAll(['td']): 
                data = cell.get_text()
                aRow.append(data.strip())
            if len(aRow) > 1:
                list_movie.append(aRow)
        i = i + 1
    
    return list_movie

print(soal1())
print('\n')
print('hasil :', soal2())
