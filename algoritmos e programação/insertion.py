lista = [ 'h', 'a', 'i','d', 'f', 'k', 'g']
lista2 = [65, 78, 98, 40, 3, 6, 12, 34, 54, 90, 80]

def insertion_sort(lista):
    for i in range(1, len(lista)): #comeca do segundo elemento
        chave = lista[i] #elemento atual a ser inserido na posicao correta
        j = i - 1 #elemento anterior
        while j >= 0 and chave < lista[j]: #compara com os elementos anteriores
            lista[j + 1] = lista[j] #desloca o elemento maior para a direita
            j -= 1
        lista[j + 1] = chave #insere o elemento na posicao correta

print("Lista original:", lista)
insertion_sort(lista)
print("Lista ordenada:", lista)

print("Lista original:", lista2)
insertion_sort(lista2)
print("Lista ordenada:", lista2)

'''comeca da esquerda para a direita, compara o elemento atual com os anteriores
e facil de entender e de implementar
e um algoritmo eficiente para listas pequenas ou quase ordenadas
e muito usado para coisas que precisam de ordenacao em tempo real

possui complexidade quadratica no pior caso 0(n2), quando a lista esta em ordem inversa
e estavel'''