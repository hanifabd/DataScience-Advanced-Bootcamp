from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

alamat = 'https://blog.sanbercode.com/'
html = urlopen(alamat)
data = bs(html)

artikel = data.findAll('div', {'class':'col-sm-12'})[1]
rows = artikel.findAll('div', {'class':'post_box_style3'})

judul = []
penulis = []

for row in rows:
    for cell in row.findAll('a', {'class':'text-dark'}):
        judul.append(cell.get_text())
    for cell in row.findAll('a', {'class':'text-muted'}):
        penulis.append(cell.get_text())

judul = [x.replace('\n                ', '') for x in judul]
penulis = [x.replace('\n                    ', '') for x in penulis]

List1 = judul.copy()
List2 = penulis.copy()

print('List1 :', List1)
print('List2 :', List2)