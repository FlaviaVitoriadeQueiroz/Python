import sys # biblioteca para manipular argumentos de linha de comando


# Etapa Map: Contagem de palavras
# Lê a entrada de dados linha por linha , da entrada padrão (stdin) 
for linha in sys.stdin:
    # Remove espaços em branco no início e no final da linha
    linha = linha.strip()
    # Divide a linha em palavras usando espaço como delimitador
    palavras = linha.split()
    # Conta o número de palavras na linha
    num_palavras = len(palavras)
    # Imprime o número de palavras na linha
    print(num_palavras)

    # Para cada palavra da linha
    for palavra in palavras:
        # Imprime a palavra com uma contagem de 1
        print(f'{palavra}\t1')

# Etapa Reduce: Agregação das contagens

palavraAtual = None # variável para armazenar a palavra atual
contagemAtual = 0 # variável para armazenar a contagem atual da palavra

# Lê o resultados intermédiarios, ordenados por palavra, linha a linha, da entrada padrão (stdin)
for linha in sys.stdin:
    # Remove espaços em branco no início e no final da linha
    linha = linha.strip()
    # Divide a linha em palavra e contagem usando tabulação como delimitador
    palavra, contagem = linha.split('\t', 1)
    # Converte a contagem para inteiro
    contador = int(contagem)

    # Se a palavra atual for diferente da palavra lida
    if palavraAtual == palavra:
        contadorAcumulado += contador # acumula a contagem da palavra atual
    else:
        # Se houver uma palavra atual, imprime a contagem acumulada
        if palavraAtual:
            print(f'{palavraAtual}\t{contadorAcumulado}')
        # Atualiza a palavra atual e a contagem acumulada
        palavraAtual = palavra
        contadorAcumulado = contador 
if palavraAtual is not None:
    print(f'{palavraAtual}\t{contadorAcumulado}') # imprime a contagem da última palavra