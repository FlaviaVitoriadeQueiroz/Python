# Essa parte é executada na GPU
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
# Até aqui era executado na GPU


# Programa principal a ser executado no host

n = 1000000 # número de elementos dos vetores
a = np.zeros(n, dtype=np.float32) # vetor de entrada a
b = np.zeros(n, dtype=np.float32) # vetor de entrada b
c = np.zeros(n, dtype=np.float32) # vetor de saída c

# Inicializa os vetores a e b com valores aleatórios
a = np.random.rand(n).astype(np.float32) # vetor de entrada a
b = np.random.rand(n).astype(np.float32) # vetor de entrada b

# Transferencia de dados do host para a GPU
a_gpu = cuda.to_device(a) # transfere/copia o vetor a para a GPU
b_gpu = cuda.to_device(b) # transfere o vetor b para a GPU
c_gpu = cuda.device_array_like(c) # cria um vetor c na GPU com o mesmo tamanho e tipo do vetor c do host, já que até então não foi calculado o vetor c, então não há necessidade de transferir o vetor c do host para a GPU, apenas criar um vetor c na GPU com o mesmo tamanho e tipo do vetor c do host.

# Cálculo das dimensões do meu grid
threadsPorBloco = 256 # número de threads por bloco
blocosPorGrid = (n + (threadsPorBloco - 1)) // threadsPorBloco # número de blocos por grid, arredondando para cima

# Chamada do kernel na GPU
soma_vetores[blocosPorGrid, threadsPorBloco](n, a_gpu, b_gpu, c_gpu) # chama o kernel na GPU
# Os parametros entre colchetes são as dimensões do grid e do bloco, respectivamente. O primeiro parâmetro é o número de blocos por grid, e o segundo parâmetro é o número de threads por bloco. O kernel será executado na GPU com essas dimensões.

# Transferencia de dados da GPU para o host
c_gpu.copy_to_host() # copia o vetor c da GPU para o host

'''Esse programa no geral explora muito o paralelismo de dados'''