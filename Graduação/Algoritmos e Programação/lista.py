lista = [1, 2, 3]

for elementos in lista:
    print(elementos)

for i in range(len(lista)):
    print(f"elemento na posicao {i}: {lista[i]}") #acesso atraves de indices

print(lista.index(2)) #retorna o indice do elemento 2