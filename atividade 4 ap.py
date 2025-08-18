#programa que simula um sistema de armazenamento de preços dos itens de hortifrutis de um supermercado 
def cadastrar_produtos(n):
    lista = []
    for _ in range(n):
        nome = input()
        if nome in lista[::2]:
            print("Produto já cadastrado")
            input()  
        else:
            preco = float(input())
            lista.append(nome)
            lista.append(preco)
    return lista

def consultar_preco(lista):
    while True:
        nome = input()
        if nome == "Fim":
            break
        if nome in lista[::2]:
            i = lista.index(nome)
            print(lista[i + 1])
        else:
            print("Produto não cadastrado")

n = int(input())
produtos = cadastrar_produtos(n)
consultar_preco(produtos)



