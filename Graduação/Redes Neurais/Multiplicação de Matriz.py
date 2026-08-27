'''simplificando a equação de multiplicação de matrizes com redes neurais
z = x * wt'''

import numpy as np

z = np.zeros((10,1))
x = np.zeros((10,5))
w = np.zeros((1,5))


# Incluindo dados fictícios para x e w
x = np.array([[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
            [26, 27, 28, 29, 30],
            [31, 32, 33, 34, 35],
            [36, 37, 38, 39, 40],
            [41, 42, 43, 44, 45],
            [46, 47, 48, 49, 50]])

w = np.array([[1, 2, 3, 4, 5]])


# Realizando a multiplicação de matrizes
z = x @ w.T  # Multiplicação de matrizes usando o operador @ (ou np.dot(x, w.T))


# Printando o resultado da multiplicação de matrizes
print("Resultado da multiplicação de matrizes (z):")
print(z)


