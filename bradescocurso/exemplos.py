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

#break = interrompe o loop quando a condição for verdadeira. Quando quero parar o loop
for n in range(1, 10):
    if n == 5:
        break  
    print(n)

#continue = pula a iteração dada na condição e continua o loop. Quando quero ignorar só uma volta do loop
for n in range(1, 6):
    if n == 3:
        continue  
    print(n)

#pass= quando preciso de um bloco de código, mas ainda não o escrevi. 
def minha_funcao():
    pass

def vi():
    return 'da Vi'
vi

#sem declarar variável, o arquivo fica aberto
open('arquivodeteste.csv', 'w').write('Curso de Python\n')

#declarando variável
arquivo = open('arquivodeteste.csv', 'a')
arquivo.write('Curso de Python do Bradesco\n')
arquivo.close()

#com with, não é necessário fechar o arquivo manualmente
with open('arquivodeteste.csv', 'a') as arquivo:
    arquivo.write('O melhor curso de python\n')

#r abre arquivos somente para leitura
#r+ abre arquivos para leitura e escrita
#w abre arquivos para sobescrever
#w+ abre arquivos para sobescrever e ler
#a abre arquivos para escrita no final do arquivo
#a+ abre arquivos para escrita no final e para leitura
