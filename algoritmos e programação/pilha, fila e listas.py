#Pilha/Stack
#Estrutura de dados do tipo LIFO (Last In, First Out), ou seja, o último elemento inserido é o primeiro a ser removido.
pilha = []

pilha.append(1)   #push, adiciona um elemento no topo da pilha
pilha.append(2)

print("Pilha após inserções:", pilha)

ultimo = pilha.pop()       # remove o elemento do topo da pilha: remove 2

print("Elemento removido:", ultimo) 
print("Fila após remoção:", pilha)

#Uso comum: chamadas de função (pilha de execução), desfazer ações (Ctrl+Z), algoritmos de backtracking, etc.


#Fila/Queue
#Estrutura de dados do tipo FIFO (First In, First Out), ou seja, o primeiro elemento inserido é o primeiro a ser removido.
from collections import deque

fila = deque()
fila.append(1)      # enqueue, adiciona um elemento no final da fila.
fila.append(2)

print("Fila após inserções:", fila)

first = fila.popleft()      # dequeue, remove o elemento do início da fila: remove 1

print("Elemento removido:", first) #dequeue
print("Fila após remoção:", fila)
#Uso comum: gerenciamento de tarefas, filas de impressão, processamento assíncrono, etc.

#Sem a biblioteca:
fila = []

fila.append('A') #enqueue
fila.append('B')
fila.append('C')

print("Fila após inserções:", fila)

primeiro = fila.pop(0)

print("Elemento removido:", primeiro) #dequeue
print("Fila após remoção:", fila)


#Lista/List
#Estrutura de dados que armazena uma sequência ordenada de elementos. Permite acesso direto a qualquer posição usando um índice.
lista = [10, 20, 30]
lista.append(40)

print("Lista após inserções:", lista)
print("Elemento removido:", lista[1]) 

lista.remove(20)    

print("Fila após remoção:", lista)
#Uso comum: armazenar coleções de dados diversos, manipulação de sequências, construção de outras estruturas de dados (como pilhas e filas).
