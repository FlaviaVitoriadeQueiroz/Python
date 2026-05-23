'''Lambda é uma função anônima, ou seja, uma função sem nome.
 Ela é usada para criar funções simples e rápidas, geralmente em uma única linha de código. A sintaxe básica de uma função lambda é:'''

# Exemplo de função lambda para calcular o quadrado de um número
quadrado = lambda x: x ** 2 
print("Quadrado de 5:", quadrado(5))

# Exemplo de função lambda para calcular a soma de dois números
soma = lambda a, b: a + b
print("Soma de 3 e 4:", soma(3, 4))

# Exemplo de função lambda para verificar se um número é par
eh_par = lambda x: x % 2 == 0   
print("O número 4 é par?", eh_par(4))

# Exemplo de função lambda para ordenar uma lista de tuplas pelo segundo elemento
lista_tuplas = [(1, 'b'), (2, 'a'), (3, 'c')]
lista_ordenada = sorted(lista_tuplas, key=lambda x: x[1])   
print("Lista ordenada:", lista_ordenada)

# Exemplo de função lambda para filtrar números pares de uma lista
numeros = [1, 2, 3, 4, 5, 6]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", numeros_pares)

# Exemplo de função lambda para mapear uma lista de números para seus quadrados
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x ** 2, numeros))
print("Números pares:", numeros_pares)
print("Quadrados dos números:", quadrados)

# Exemplo de função lambda para reduzir uma lista de números somando-os
from functools import reduce
numeros = [1, 2, 3, 4, 5]
soma_total = reduce(lambda x, y: x + y, numeros)
print("Soma total:", soma_total)
print("Quadrado de 5:", quadrado(5))
print("Soma de 3 e 4:", soma(3, 4))


'''Ela é muito usada quando você precisa de uma função simples e rápida, normalmente em operações como:
map()
filter()
sorted()
reduce()

Sintxe da função lambda:
lambda argumentos: expressão
'''