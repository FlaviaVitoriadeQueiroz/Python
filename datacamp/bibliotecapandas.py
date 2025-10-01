#linhas = observacoes
#colunas = atributos

'''vendas_manuais = [
    {"id": 1, "produto": "Camisa", "quantidade": 2, "preço": 59.90, "data": "2025-01-30"},
    {"id": 2, "produto": "Tênis", "quantidade": 1, "preço": 249.90, "data": "2025-05-30"},
    {"id": 3, "produto": "Calça", "quantidade": 3, "preço": 129.90, "data": "2025-05-05"},
    {"id": 4, "produto": "Jaqueta", "quantidade": 4, "preço": 199.90, "data": "2025-04-24"},
    {"id": 5, "produto": "Bermuda", "quantidade": 7, "preço": 89.90, "data": "2025-03-30"},
    {"id": 6, "produto": "Blusa", "quantidade": 5, "preço": 79.90, "data": "2025-02-27"},
    {"id": 7, "produto": "Salto", "quantidade": 2, "preço": 556.78, "data": "2025-01-18"},
    {"id": 8, "produto": "Sapatilha", "quantidade": 3, "preço": 99.95, "data": "2025-02-09"},
    {"id": 9, "produto": "Bota", "quantidade": 8, "preço": 255.99, "data": "2025-01-12"},
    {"id":10, "produto": "Camiseta", "quantidade": 15, "preço": 25.95, "data": "2025-01-07"},
    {"id": 11, "produto": "Saia", "quantidade": 20, "preço": 49.99, "data": "2025-04-15"},
]'''
#Cada elemento da lista é um dicionário representando um registro único (uma venda).
#Ideal quando você trabalha com linhas de dados (vendas, clientes, etc.).

dict = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasília", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}
#Cada chave do dicionário representa uma coluna (ex: "country", "capital", "area", "population").
#Os valores são listas com os dados de cada linha.
#Essa estrutura é ótima para ser convertida em um DataFrame do pandas.

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

brics.index = ['BR', 'RU', 'IN', 'CH', 'SA']
print(brics)

brics1 = pd.read_csv("B:/VScode/Python/cursos/brics.csv", index_col=0) #index_col=0 para usar a primeira coluna como indice, em vez de criar um novo indice numerico
print(brics1)

#exercicio 1
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

import pandas as pd

my_dict = {
        'country': names,
        'drives_right': dr,
        'cars_per_cap': cpc
}

cars = pd.DataFrame(my_dict)

print(cars)

#exercicio 2
import pandas as pd

names1 = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr1 =  [True, False, False, False, True, True, True]
cpc1 = [809, 731, 588, 18, 200, 70, 45]
cars_dict1 = { 'country':names1, 'drives_right':dr1, 'cars_per_cap':cpc1 }
cars1 = pd.DataFrame(cars_dict1)
print(cars1)

row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

cars1.index = row_labels

print(cars1)

#exercicio 3
import pandas as pd

cars2 = pd.read_csv("cars.csv")

print(cars2)

#exercicio 4
import pandas as pd

cars3 = pd.read_csv('cars.csv', index_col=0)

print(cars3)