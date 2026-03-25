#compreensão de listas
#tradicional
lista = []
for i in range(9, 18):
    lista.append(i)
print(lista)

lista = []
for i in range(9, 18):
    lista.append(i *3)
print(lista)

lista= []
for i in range(9, 18, 3):
    lista.append(i)
print(lista)

#compreensão
lista = [i for i in range(9, 18)]
print(lista)

lista = [i*3 for i in range(9, 18)]
print(lista)

#é diferente para tuplas
tupla = tuple(i for i in range(9, 18))
print(tupla)

#é diferente para dicionários
dicionario = {i: i for i in range(9,18)}
print(dicionario)

#é diferente para conjuntos
conjuntos = {i**2 for i in range(5)}
print(conjuntos)

#Lista	[expressão for item in iterável]	[i**2 for i in range(5)]
#Tupla	tuple(expressão for item in iterável)	tuple(i**2 for i in range(5))
#Conjunto	{expressão for item in iterável}	{i**2 for i in range(5)}
#Dicionário	{chave: valor for item in iterável}	{i: i**2 for i in range(5)}

#emunerate():
#sem enumerate():
nomes = ['Vitória', 'Alfredo', 'João', 'Flávia', 'Henrique', 'Ana', 'Eloísa']
indice = 1
for nome in nomes:
    print(indice, nome)
    indice += 1

#com enumerate():
nomes = ['Vitória', 'Alfredo', 'João', 'Flávia', 'Henrique', 'Ana', 'Eloísa']
for indice, nome in enumerate(nomes, start=1):
    print(indice, nome)


while nome == 'sair':
    break 

#função zip() = percorre diversas listas ao mesmo tempo
lista1 = [3, 6, 9, 12, 15, 18]
lista2 = ['F', 'V', 'Q', 'Z', 'A', 'H', 'P']
for f, v in zip(lista1, lista2):
    print(f, v)
#o zip vai acabar assim que  a menor lista acabar:
lista1 = [1, 2]
lista2 = ['a', 'b', 'c']
#contas:

a = [10, 20, 30]
b = [1, 2, 3]
somas = [x + y for x, y in zip(a, b)]
print(somas)

#comparações:
respostas = ['a', 'b', 'c']
gabarito = ['a', 'c', 'c']
acertos = 0
for r, g in zip(respostas, gabarito):
    if r == g:
        acertos += 1
print(f'Acertos: {acertos}')

resposta1 = ['a', 'a', 'c', 'd', 'c', 'e']
resposta2 = ['b', 'a', 'c', 'e', 'e', 'd']
gabarito= ['b', 'a', 'c', 'a', 'c', 'd']
acertos1 = 0
acertos2 = 0
for g, r1, r2 in zip(gabarito, resposta1, resposta2): #é necessário declarar o gabarito também para ser comparadas as respostas e não a lista inteira
    if g == r1:
        acertos1 += 1
    if g == r2:
        acertos2 +=1
print(f'Acertos da prova 2: {acertos2}', f'Acertos da prova 1: {acertos1}')

#desfazendo o zip
pares = [(1, 'a'), (2, 'b'), (3, 'c')]
numeros, letras = zip(*pares)
print(numeros)  
print(letras)

#zip com dicionários:
aluno1 = {'nome': 'Ana', 'nota': 9}
aluno2 = {'nome': 'Bruno', 'nota': 7}
for valor1, valor2 in zip(aluno1.values(), aluno2.values()): #values() retorna somente os valores do dicinarios
    print(valor1, valor2)

#else com for ou while = é usado como uma continuação do loop, ou seja, se o loop não for interrompido, o else srá executado
#else e for:
#aqui não vai ser executado o else, pois o loop é interrompido no break:
numeros = [1, 3, 5, 7, 4, 9]
for n in numeros:
    if n == 4:
        print("Número 4 encontrado!")
        break
else:
    print("Número 4 não está na lista.")

#já aqui o else será executado:
numeros = [1, 3, 5, 7, 9]
for n in numeros:
    if n == 4:
        print("Número 4 encontrado!")
        break
else:
    print("Número 4 não está na lista.")

#else e while:
c = 1
while c <= 3: #enquanto
    print(f"Tentativa {c}")
    c += 1
else:
    print("Loop terminou normalmente.")

#O else em loops é útil, por exemplo:
#Quando é necessário procurar algo numa lista e quer fazer algo se não encontrar.
#Quando se quer verificar se um loop rodou por completo, sem interrupção.
