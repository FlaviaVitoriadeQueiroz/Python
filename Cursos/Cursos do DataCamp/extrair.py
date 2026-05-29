#  extraindo dados de uma API 

import requests 

# requests é uma biblioteca para fazer requisições HTTP em Python.
# o método get() é usado para fazer uma requisição GET, que é usada para solicitar dados de um recurso específico.
# o método post() é usado para fazer uma requisição POST, que é usada para enviar dados para um recurso específico.

response = requests.get('https://www.datacamp.com/')
print(response.status_code)

# or

url = 'https://www.datacamp.com/'
response = requests.post(url)
  


# transformando em um objeto python
data = response.json()
print(data)




# se conectando a um banco de dados

import sqlalchemy

connnection_string = 'postgresql://username:password@localhost:5432/mydatabase'
engine = sqlalchemy.create_engine(connnection_string)   




# extraindo dados de um arquivo CSV

import pandas as pd
data = pd.read_csv('data.csv')
print(data.head())

