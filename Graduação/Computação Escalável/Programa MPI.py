from mpi4py import MPI
import numpy as np

com = MPI.COMM_WORLD # cria um comunicador global, que é um objeto que permite a comunicação entre os processos MPI
idProcesso = com.Get_rank() # obtém o identificador do processo atual, que é um número inteiro único para cada processo MPI
nProcessos = com.Get_size() # obtém o número total de processos MPI