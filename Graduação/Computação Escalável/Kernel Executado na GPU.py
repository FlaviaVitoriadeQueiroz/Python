# Usa o compilador NUMBA para traduzir o código Python para CUDA 
from numba import cuda
import numpy as np

'''Um Kernel é uma função que é executada na GPU. Ele é chamado de "kernel" porque é a 
parte central do código que será executada em paralelo em muitos threads na GPU.'''

@cuda.jit #marca a função como um kernel CUDA, que será executado na GPU
def soma_vetores(n, a, b, c): # n = dimensão dos vetores, a = vetor de entrada, b = vetor de entrada, c = vetor saída
    # determina a posição dos vetores atribuídos a cada thread
    i = cuda.bloclIx.x * cuda.blockDim.x + cuda.threadIdx.x # cálculo fornecido pelo CUDA para determinar o índice global da thread
    # cada thread calcula um elemento do vetor c
    if i < n: # só para garantir que no último bloco, caso o tamanho dos vetores não seja múltiplo do número de threads por bloco, no último bloco posso ter algumas threads que não vão ter trabalho. Ou seja, para garantir que não seja acessada posições inválidas 
        c[i] = a[i] + b[i]
    # não é necessário que aja um laço for, pois cada thread é responsável por um elemento do vetor c, e o CUDA gerencia a execução paralela das threads.