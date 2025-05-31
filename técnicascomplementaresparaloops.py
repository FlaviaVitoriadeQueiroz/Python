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