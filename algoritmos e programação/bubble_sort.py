lista = [ 'h', 'a', 'i','d', 'f', 'k', 'g']
lista2 = [65, 78, 98, 40, 3, 6, 12, 34, 54, 90, 80]

def bubble_sort(lista):
    n = len(lista) #identifica o tamanho da lista
    for i in range(n): #percorre toda a lista
        for j in range(0, n - i - 1): #compara cada par de elementos adjacentes
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j] #troca se estiver fora de ordem

print("Lista original:", lista)
bubble_sort(lista)
print("Lista ordenada:", lista)

print("Lista original:", lista2)
bubble_sort(lista2)
print("Lista ordenada:", lista2)

'''comeca da esquerda para a direita, o elemento atual com os proximos

E um algoritmo simples
um dos metodos mais classicos

tempo de execucao maior 0(n^2), por causa dos dois loops aninhados
pouco eficiente em listas grandes

e um elemento estavel, ou seja mantem a ordem dos elementos iguais

considera o ultimo elemento ordenado'''