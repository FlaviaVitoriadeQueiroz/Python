from mpi4py import MPI
import numpy as np

# Programa principal
com = MPI.COMM_WORLD # cria um comunicador que inclui todos os processos
idProcesso = com.Get_rank() # obtém o identificador do processo atual
nProcessos = com.Get_size() # obtém o número total de processos

if idProcesso == 0: #processo raiz/mestre
    # Inicialização vetor com nProcessos elementos inteiros
    vetor = np.arange(nProcessos, dtype='i') # cria um vetor de inteiros de 0 a nProcessos-1
    print(f'Processo {idProcesso} enviando vetor: {vetor}')

    # Envia um elemento do vetor para um dos demais processos
    for i in range(1, nProcessos):
        com.send(vetor[i], dest=i) # envia o elemento vetor[i] para o processo com id i
        print(f'Processo {idProcesso} enviando elemento {vetor[i]} para processo {i}')
else: #processos escravos/demais processos
    dado = np.zeros(1, dtype='i') # cria um vetor de tamanho 1 para receber o dado
    dado[0] = com.recv(source=0) # recebe o dado do processo raiz
    print(f'Processo {idProcesso} recebeu elemento {dado[0]} do processo 0')

