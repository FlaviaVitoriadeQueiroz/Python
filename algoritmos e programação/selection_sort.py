'''organizacao por selecao direta, selecionando o menor elemento do conjunto, para so realizara troca no final como um todo

considera o primeiro elemento como o menor, ou seja, ordenado

tem um numero reduzido de trocas, porem um numero elevado de comparacoes
boa acao para cenarios onde a troca de elementos e mais custosa que a comparacao (disco rigido, memoria flash)

pouco eficiente em listas grandes
complexo de caso 0(n2) no melhor e pior caso
nao e estavel, ou seja, nao mantem a ordem dos elementos iguais'''

lista = [ 'h', 'a', 'i','d', 'f', 'k', 'g']
lista2 = [65, 78, 98, 40, 3, 6, 12, 34, 54, 90, 80]


def selection_sort(lista):
    n = len(lista) #identifica o tamanho da lista
    for i in range(n): #percorre toda a lista
        indice_menor = i #considera o primeiro elemento como o menor

        for j in range(i + 1, n): #compara com os elementos seguintes
            if lista[j] < lista[indice_menor]:
                indice_menor = j #atualiza o indice do menor elemento 
        if indice_menor != i:
            lista[i], lista[indice_menor] = lista[indice_menor], lista[i] #troca o menor elemento com o primeiro elemento

print("Lista original:", lista)
selection_sort(lista)
print("Lista ordenada:", lista)

print("Lista original:", lista2)
selection_sort(lista2)
print("Lista ordenada:", lista2)