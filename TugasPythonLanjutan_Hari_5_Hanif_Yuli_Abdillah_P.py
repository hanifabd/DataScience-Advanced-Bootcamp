from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

alamat = 'https://pokemondb.net/pokedex/all'
req = Request(alamat, headers={'User-Agent' : 'Mozilla/5.0'})
html = urlopen(req)
data = bs(html, 'html.parser')

table = data.find('table', {'id' : 'pokedex'})
rows = table.findAll('tr', limit=985)

pokes = []
for row in rows:
    poke_datas = []
    for data in row.findAll(['th','td']):
        poke_data = data.get_text()
        poke_datas.append(poke_data)
    pokes.append(poke_datas)

df_pokes = pd.DataFrame(pokes)
df_pokes_head = df_pokes.iloc[0]
df_pokes.columns = df_pokes_head
df_pokes = df_pokes[1:]
df_pokes.reset_index(drop=True)

df_pokes = df_pokes.astype({'Attack': int, 'Defense': int})

X = df_pokes[['Attack', 'Defense']]
km = KMeans(n_clusters=3, random_state=0)
cluster = km.fit_predict(X)
df_pokes['Cluster'] = cluster

plt.scatter(df_pokes['Attack'], df_pokes['Defense'], c=df_pokes['Cluster'], s=5)
plt.title("Hasil Klustering K-Means")
plt.xlabel("Atk")
plt.ylabel("Def")
plt.show()

# Kesimpulan
# 1. Menurut saya KMeans cukup cepat dalam melakukan clustering
# 2. Solusi selalu ditemukan, tetapi terdapat kemungkinan bias
# 3. Sensitif terhadap inisialisasi centroid awal
# 4. Sensitif terhadapa data pencilan(outliers)