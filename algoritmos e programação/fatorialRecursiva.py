n = int(input("Digite um número: "))

def fatorial(n):
    if n == 0 or n == 1:
        return 1 #se for 0 ou 1 o resultado sera 1
    return n * fatorial(n - 1) #chama a funcao novamente, ate chegar em 0 entao retorna o valor 

print(f"O fatorial de {n} é {fatorial(n)}") #a ordem de retorno funciona como uma pilha, entao o ultimo a entrar e o primeiro a sair. E os resultados precisam ser empilhados para serem armazenados durante o processo

'''Vantagens: clareza e simplicidade do codigo
Desvantagens: aumneta o custo operacional, pois cada chamada de funcao consome memoria e tempo de processamento
dificuldade de depuracao, pois o rastreamanto de erros pode ser mais complexo em funcoes recursivas
risco de esturouro de pilha (stack overflow), se a recursao for muito profunda. Por isso precisa ter um fim bem definido
consome mais memoria e processador que a versao interativa
E usada em: fatorial, sequencia de fibonaci, busca em estruturas de dados como arvores e grafos
Quando usar? quando o problema pode ser quebrado em subproblemas menores e para solucoes de multiplos caminhos (blacktracking, labirintos e sudoku)

Em python a recursao tem limite de profundidade padrao de 1000 chamadas, mas pode ser alterada com a biblioteca sys, usando sys.setrecursionlimit(novo_limite)'''

#Outro exemplo de recursao
def somar(numeros):
    if not numeros: #se a lista estiver vazia
        return 0
    return numeros[0] + somar(numeros[1:])

lista = [18, 9, 12, 21]

print(f"A soma dos elementos da lista {somar(lista)}")