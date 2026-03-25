dict = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasília", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

import pandas as pd
brics = pd.DataFrame(dict)
brics.index = ['BR', 'RU', 'IN', 'CH', 'SA']

#acessando somente a coluna country
print(brics['country']) #assim recebemos uma saida diferente do esperedo: Name: country, dtype: object
print(brics.country) #outra forma de acessar a coluna country
print(type(brics['country'])) #pandas.core.series.Series = matriz unidimencional
#varias series juntas = DataFrame

#para resolver o problema e so usar dois colchetes
print(brics[['country']]) #assim recebemos um DataFrame
print(type(brics[['country']])) #pandas.core.frame.DataFrame = matriz bidimencional

#para acessar mais de uma coluna
print(brics[['country', 'capital']])

#para acessar as linhas usamos o loc e iloc, mas parecido com o que vimos em numpy
print(brics.loc['IN']) #acessa a linha com o indice IN
print(type(brics.loc['IN'])) #pandas.core.series.Series = matriz unidimencional

print(brics.iloc[2]) #acessa a linha de indice 2
print(type(brics.iloc[2])) #pandas.core.series.Series = matriz unidimencional

print(brics.loc[['IN', 'RU']]) #acessa as linhas com os indices IN e RU
print(type(brics.loc[['IN', 'RU']])) #pandas.core.frame.DataFrame = matriz bidimencional

print(brics[1:4]) #acessa as linhas de indice 1 a 3

print(brics.loc[['IN', 'RU'], ['country', 'capital']]) #acessa as linhas com os indices IN e RU e as colunas country e capital

print(brics.loc[:, ['country', 'capital']]) #acessa country e capital de todas as linhas

print(brics.iloc[[1, 2, 3], [0, 1]]) #acessa as linhas de indice 1, 2 e 3 e as colunas de indice 0 e 1

#exercicio 1
'''import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

print(cars['country'])

print(cars[['country']])

print(cars[['country', 'drives_right']])'''

#exercicio 2
'''import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

print(cars.iloc[0:3])

print(cars.iloc[[3, 4, 5]])'''

#exercicio 3
'''import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

print(cars.loc['JPN'])

print(cars)
print(cars.loc[['AUS', 'EG']])'''

#exercicio 4
'''import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

print(cars)
print(cars.loc['MOR', 'drives_right'])

subset = cars.loc[['RU', 'MOR'], ['country', 'drives_right']]
print(subset)'''

#exercicio 5
'''import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

print(cars['drives_right'])

print(cars[['drives_right']])

print(cars[['cars_per_cap', 'drives_right']])'''