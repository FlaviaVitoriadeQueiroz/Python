#estruturas de repetição
# for, while, break, continue, pass
#para, enquanto, interromper, continuar, passar]

#for = sabemos quantas vezes vai reprtir
for n in range(18):
    print(n)
#vai executar até que n seja 17
#se não queremos que o valor inicial seja 0, é necessário utilizar o range:
for n in range(9, 18):
    print(n)

#while = não sabemos qunatas vezes vai repetir, repetirá até quando a condição for verdadeira
v = 9
while v <= 18:
    print('da Vi')
    v+= 1
#é necessário guradrar o valor de v, senão ele vai ficar imprimindo 9

def vi():
    return 'da Vi'
vi

open('open', 'w')
open.write('Bradesco Curso de Python\n') #***.write() vai escrever no arquivo
open.close()

arquivo = open('open', 'w')
arquivo.write('Curso de Python do Bradesco\n')
arquivo.close()

with open('open', 'w') as arquivo:
    arquivo.write('O melhor curso de python\n')

#r abre arquivos somente para leitura
#r+ abre arquivos para leitura e escrita
#w abre arquivos para sobescrever
#w+ abre arquivos para sobescrever e ler
#a abre arquivos para escrita no final do arquivo
#a+ abre arquivos para escrita no final e para leitura