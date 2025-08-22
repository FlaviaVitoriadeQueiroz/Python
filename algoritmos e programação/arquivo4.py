#tratando excecoes em arquivos
#usado para arquivos, banco de dados etc
try:
    with open("vendas.csv", "r") as arquivo:
        dados = arquivo.read()
    print(dados)
except FileNotFoundError:
    print('Arquivo nao encontrado')
