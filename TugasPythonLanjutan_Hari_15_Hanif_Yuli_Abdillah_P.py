import openpyxl as oxl
import json

path = 'pokemon_db.xlsx'
wb = oxl.load_workbook(path)
sheet = wb.active

pokemon_data = []
for row_index in range (len(sheet['A'])):
    if sheet[row_index+1][0] == "Nama":
        continue
    pokemon = {}
    pokemon['Name']=sheet[row_index+1][0].value
    pokemon['Type']=sheet[row_index+1][1].value
    pokemon['Total']=sheet[row_index+1][2].value
    pokemon['HP']=sheet[row_index+1][3].value
    pokemon['Attack']=sheet[row_index+1][4].value
    pokemon['Defense']=sheet[row_index+1][5].value
    pokemon['Sp.Atk']=sheet[row_index+1][6].value
    pokemon['Sp.Def']=sheet[row_index+1][7].value
    pokemon['Speed']=sheet[row_index+1][8].value
    pokemon_data.append(pokemon)

with open('hanif.uxlearn.json', 'w') as f:
    json.dump(pokemon_data, f)