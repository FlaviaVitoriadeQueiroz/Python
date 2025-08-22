#tratando excecoes em arquivos
try:
    with open("vendas.csv", "r") as arquivo:
        dados = arquivo.read()
    print(dados)
except FileNotFoundError:
    print('Arquivo nao encontrado')
