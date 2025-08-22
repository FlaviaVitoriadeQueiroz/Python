with open("B:\\VScode\\Python\\ap\\Book1.csv", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
''' read() → lê todo o conteúdo como uma única string.
readline() → lê uma linha por vez.
readlines() → lê todas as linhas, e retorna uma lista de strings (uma por linha).'''


with open("vendas.csv", "a", encoding="utf-8") as arquivos:
    for linhas in arquivos:
        arquivos.write("Pascal\n")
    print(arquivos)
