n = int(input("Digite um numero:"))

def fatorial(n):
    resultado = 1 #define que o resultado comeca em 1, sendo 1 para 0 e 1, que nao entram no loop
    for i in range(2, n + 1): #vai comecar do 2, pq o fatorial de 0 e 1 e 1. E n + 1 pq o range para antes do ultimo numero
        resultado *= i #multiplica o resultado pelo numero atual do loop
    return resultado

print(f"O fatorial de {n} e {fatorial(n)}")

"""Vantagens: reutiliza o mesmo espaco de memoria, nao aumentando o custo operacional
e mais rapida, pois nao ha o overhead das chamadas de funcao
E usada em: c ontadores, lacos de soma, percorrer arrays"""