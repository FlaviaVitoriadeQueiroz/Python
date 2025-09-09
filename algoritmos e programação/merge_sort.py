#dividir para conquistar, divide em duas metades, ate que cada sublista tenha um elemento e depois junta as sublistas em ordem crescente
#complexidade 0(nlogn)
#nao tem laco alinhado

lista = [ 'h', 'a', 'i','d', 'f', 'k', 'g']
lista2 = [65, 78, 98, 40, 3, 6, 12, 34, 54, 90, 80]

def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[meio:]
        direita = lista[:meio]

        #chama a funcao recursivamente para as duas metades
        merge_sort(esquerda)
        merge_sort(direita)

        #juncao das duas metades
        i = j = k = 0 #inicializando os indices
        while i < len(esquerda) and j < len(direita): #esse lacp so encrementa os menores elementos 
            if esquerda[i] < direita[j]: #se o elemento da esquerda for menor
                lista[k] = esquerda[i] #coloca o elemento da esquerda na posicao k da lista original
                i +=1 #incrementa o indice da esquerda
            else:
                lista[k] = direita[j] #coloca o elemento da direita na posicao k da lista original
                j += 1 #incrementa o indice da direita
            k += 1 #incrementa o indice da lista original independentemente de qual lado veio o elemento 

        #adiciona os elementos restantes, pois o primeiro while termina quando uma das metades acaba
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

#Usando
print("Lista original:", lista)
merge_sort(lista)
print("Lista ordenada:", lista)

print("Lista original:", lista2)
merge_sort(lista2)
print("Lista ordenada:", lista2)
