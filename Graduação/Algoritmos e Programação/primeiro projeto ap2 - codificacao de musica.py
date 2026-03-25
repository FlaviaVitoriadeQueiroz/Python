import os

def substituir_vogais(texto):
    resultado = ""
    for caractere in texto:
        if caractere in "Aa":
            resultado += "!"
        elif caractere in "Ee":
            resultado += "@"
        elif caractere in "Ii":
            resultado += "#"
        elif caractere in "Oo":
            resultado += "$"
        elif caractere in "Uu":
            resultado += "%"
        else: 
            resultado += caractere
    return resultado 

def processar_arquivo(entrada, saida):
    try:
        with open(entrada, 'r', encoding = 'latin-1') as arquivo_entrada:
            conteudo = arquivo_entrada.read()
        
        conteudo_codificado = substituir_vogais(conteudo)
        with open(saida, 'w', encoding = 'utf-8') as arquivo_saida:
            arquivo_saida.write(conteudo_codificado)

        caminho_completo = os.path.abspath(saida)
        print(f'Arquivo processado com sucesso! Texto codificado salvo em em:\n{caminho_completo}')

    except FileNotFoundError:
        print("Erro: Arquivo de entrada nao encontrado")
    except Exception as e:
        print(f'Erro inesperado {e}')

arquivo_entrada = "B:\\VScode\\Python\\ap\\Musica.txt"
arquivo_saida = input("Digite o nome do arquivo de saida: ")
if not arquivo_saida.endswith('.txt'):
    arquivo_saida += '.txt'
processar_arquivo(arquivo_entrada, arquivo_saida)

