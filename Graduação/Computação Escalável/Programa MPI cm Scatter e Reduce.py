from mpi4py import MPI
import numpy as np

# Programa principal
com = MPI.COMM_WORLD # cria um comunicador que inclui todos os processos
idProcesso = com.Get_rank() # obtém o identificador do processo atual
nProcessos = com.Get_size() # obtém o número total de processos

n = 10 # tamanho do vetor a ser distribuído
if idProcesso == 0: #processo raiz/mestre
    # Inicialização vetor com n elementos inteiros
    vetor = np.arange(n, dtype='i') # cria um vetor de inteiros de 0 a n-1
    print(f'Processo {idProcesso} enviando vetor: {vetor}')

    # Envia o vetor para todos os demais processos
    for i in range(1, nProcessos):
        com.send(vetor, dest=i) # envia o vetor para o processo com id i
        print(f'Processo {idProcesso} enviando vetor para processo {i}')
else: #processos escravos/demais processos
    dado = np.zeros(n, dtype='i') # cria um vetor de tamanho n para receber o dado
    dado[:] = com.recv(source=0) # recebe o vetor do processo raiz
    print(f'Processo {idProcesso} recebeu vetor: {dado} do processo 0')

# Parte do vetor que cada processo vai receber
parte_vetor = np.zeros(n//nProcessos, dtype='i') # cria um vetor de tamanho n/nProcessos para receber a parte do vetor

# Distribuição do vetor usando Scatter
com.Scatter(vetor, parte_vetor, root=0) # distribui o vetor do processo raiz para todos os processos
print(f'Processo {idProcesso} recebeu parte do vetor: {parte_vetor}')

soma_local = np.sum(parte_vetor) # cada processo calcula a soma da sua parte do vetor
print(f'Processo {idProcesso} soma local: {soma_local}')

# Obtenção da soma global usando Reduce
soma_global = np.zeros(1, dtype='i') # cria um vetor de tamanho 1 para receber a soma global
com.Reduce(soma_local, soma_global, op=MPI.SUM, root=0) # reduz a soma local de todos os processos para o processo raiz usando a operação de soma
if idProcesso == 0: # processo raiz
    print(f'Processo {idProcesso} soma global: {soma_global[0]}') # imprime a soma global no processo raiz  