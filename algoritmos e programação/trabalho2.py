import random

lista_original = []

for i in range(100):
    numero = random.randint(1, 1000)
    lista_original.append(numero)

print('Lista Original:', lista_original)

lista_pares= []
lista_impares= []

for numero in lista_original:
    if numero % 2 == 0:
        lista_pares.append(numero)
    elif numero % 2 != 0:
        lista_impares.append(numero)

print('Lista de Numeros Pares:', lista_pares)
print('Lista de Numeros Impares:', lista_impares)