import numpy as np

# Definindo os valores das matrizes de entrada (x) e pesos (w)
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

w = np.array([[1, 1, 1], [2, 2, 2]])


print('X: ', x.shape, 'W: ', w.shape)
print("Matriz de entrada (x):")
print(x)
print("\nMatriz de pesos (w):")
print(w)


'''o produto escalar = @'''

z = x @ w.T  # Multiplicação de matrizes usando o operador @ (ou np.dot(x, w.T))
print('Z:\n', z)


