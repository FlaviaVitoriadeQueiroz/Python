lista = [ 'h', 'a', 'i','d', 'f', 'k', 'g']
lista2 = [65, 78, 98, 40, 3, 6, 12, 34, 54, 90, 80]

def insertion_sort(lista):
    for i in range(1, len(lista)): #comeca do segundo elemento
        chave = lista[i] #elemento atual
        j = i - 1 #elemnto anterior
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