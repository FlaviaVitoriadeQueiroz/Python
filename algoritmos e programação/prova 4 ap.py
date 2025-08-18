n = int(input()) # Lê um número inteiro fornecido pelo usuário
a, b = 1, 1 # Inicializa os dois primeiros termos da sequência de Fibonacci
contador = 0 # Inicializa o contador que armazenará a quantidade de termos da sequência menores ou iguais a 'n'
while a <= n: # Executa o laço enquanto o termo atual 'a' for menor ou igual a 'n'
    contador += 1 # Incrementa o contador
    a, b = b, a + b # Atualiza os dois termos da sequência de Fibonacci

print(contador) # Exibe o total de termos da sequência de Fibonacci que são menores ou iguais a 'n'

