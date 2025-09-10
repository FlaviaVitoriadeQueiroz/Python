#ordenacao rapida
#tambem se baseia no metodo dividir para conquistar

#escolhe um elemento como pivô e particiona a lista em dois subarrays, de acordo com o pivô
#os elementos menores que o pivô vao para a esquerda e os maiores para a direita
#depois aplica a mesma logica recursivamente para os subarrays

#complexidade 0(nlogn) no melhor e medio caso, mas pode chegar a 0(n2) no pior caso 

#como escolher o pivô?
 #pode ser o primeiro elemento, o ultimo, a mediana ou um elemento aleatorio ou do meio

lista = [ 'h', 'a', 'i','d', 'f', 'k', 'g']
lista2 = [65, 78, 98, 40, 3, 6, 12, 34, 54, 90, 80]
lista3 = [5, 2, 1, 4, 5, 2, 1, 4]


def quick_sort(lista):
    if len(lista) <= 1: #caso base
        return lista
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x <= pivo] #se tiver elemento menor que o pivo. comprenssao de lista
        maiores = [x for x in lista[1:] if x > pivo] #se tiver elemento maior que o pivo
        return quick_sort(menores) + [pivo] + quick_sort(maiores) #passo recursivo

#Usando
print("Lista original:", lista)
lista = quick_sort(lista)
print("Lista ordenada:", lista)

print("Lista original:", lista2)
lista2 = quick_sort(lista2)
print("Lista ordenada:", lista2)

print("Lista original:", lista3)
lista3 = quick_sort(lista3)
print("Lista ordenada:", lista3)