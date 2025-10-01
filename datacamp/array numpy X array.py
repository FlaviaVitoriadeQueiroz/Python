import numpy as np

# Criando um array unidimensional (vetor)
lista_py = [1, 2, 3, 4, 5]
array_np = np.array(lista_py)
print(array_np)

# Criando um array bidimensional (matriz)
lista_de_listas = [[1, 2, 3], [4, 5, 6]]
array_matriz = np.array(lista_de_listas)
print(array_matriz)

'''por que usar pandas e nao numpy?
numpy so suporta array com o mesmo tipo de dados, enquanto pandas suporta diferentes tipos de dados em um unico DataFrame.'''


'''diferenca entre array e array com numpy:
Lista/array comum do Python (list): pode guardar qualquer tipo de dado misturado (números, strings, objetos…).
Listas não são otimizadas para cálculos matemáticos. Se você quiser somar duas listas, precisa percorrer os elementos com um loop.
Listas não suportam diretamente operações como soma, multiplicação, raiz quadrada, média, etc.

Array do NumPy (numpy.ndarray): é feito para armazenar apenas dados do mesmo tipo (geralmente números) de forma muito mais eficiente.
NumPy arrays são otimizados em C e conseguem fazer cálculos em vetorização (operações em todos os elementos de uma vez), o que é muito mais rápido.
Arrays NumPy já têm funções prontas: np.mean(), np.sum(), np.sqrt(), etc.'''

lista = [1, 2, 3, 4]
array = np.array([1, 2, 3, 4])

# Soma elemento por elemento
# Lista precisa de loop
lista_somada = [x + 2 for x in lista]

# NumPy faz direto
array_somado = array + 2

print(lista_somada)  # [3, 4, 5, 6]
print(array_somado)  # [3 4 5 6]
