arquivo = open('open.csv', 'w', encoding = 'utf-8')
arquivo.write('Nome: Flávia, Idade:19, Cidade: Colina\n')
arquivo.write('Nome: Alfredo, Idade: 21, Cidade: Barretos\n')

arquivo.close()

arquivo = open('open.csv', 'a', encoding = 'utf-8')
arquivo.write('Nome: Henrique, Idade: 10, Cidade: Colina\n')

arquivo.close()

arquivo = open('open.csv', 'r', encoding = 'utf-8')
print(arquivo.read())

