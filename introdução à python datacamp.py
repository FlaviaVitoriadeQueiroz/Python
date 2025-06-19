#Para imprimir o tipo de uma variável
v = 189026
print(type(v))

#Para copiar uma lista e não alterar a original
lista = [3, 6, 9, 12, 15, 18, 21]
lista_copia = lista[:]
lista_copia[6] = 3
print(lista)
print(lista_copia)

#Para ver a documentação de uma função
help(round)

#Pow calcula a potência de um mnúmero
pow (3, 9)
#O primeiro número corresponde à base e o segundo ao expoente, é possível ter um terceiro número que corresponde ao módulo
print(pow(3, 9))
#Pow com móculo
pow (3, 9, 2)
print(pow(3, 9, 2))
#o módulo realiza a potência modular, que seria o resto da divisão do resultado da potência pelo módulo, igual a 2**

#Ordena elementos sem mudar a lista oroginal
l = [2, 6, 1, 9, 0, 3, 5, 4]
#sorted(l, key=None, reverse= False) 
#key define a base da ordenação, pode ser none(é o comportamneto padrão, não faz nada), len(pelo comprimento), lamba(usa o ultimo caracter de cada "palavra" entre outros
#reverse define se a ordenação é crescente (false) ou decrescente (true)
ordenar= sorted(l, reverse=True)
print(ordenar)
#Sort volta a lista a forma original
ordenar= sorted(l, reverse=True).sort()
print(ordenar)
print(l)

#index retorna o índice do elemento na lista
#Se o elemento não existir, retorna erro
f = [1, 2, 6, 9, 3]
f.index(9)
print(f.index(9))

#replace substitui uma parte de uma string por outra
#A função replace recebe dois argumentos, o primeiro é a parte que será substituída e o segundo é o que irá substituir
frase = 'Python é uma linguagem de programação'
print(frase.replace('Python', 'SQL'))

import numpy as np

