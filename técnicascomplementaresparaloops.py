#compreensão de listas
#tradicional
lista = []
for i in range(9, 18):
    lista.append(i)
print(lista)

lista = []
for i in range(9, 18):
    lista.append(i *3)
print(lista)

lista= []
for i in range(9, 18, 3):
    lista.append(i)
print(lista)

#compreensão
lista = [i for i in range(9, 18)]
print(lista)

lista = [i*3 for i in range(9, 18)]
print(lista)

#é diferente para tuplas
tupla = tuple(i for i in range(9, 18))
print(tupla)

#é diferente para dicionários
dicionario = {i: i for i in range(9,180)}
print(dicionario)

#é diferente para conjuntos
conjuntos = {i**2 for i in range(5)}
print(conjuntos)

#Lista	[expressão for item in iterável]	[i**2 for i in range(5)]
#Tupla	tuple(expressão for item in iterável)	tuple(i**2 for i in range(5))
#Conjunto	{expressão for item in iterável}	{i**2 for i in range(5)}
#Dicionário	{chave: valor for item in iterável}	{i: i**2 for i in range(5)}