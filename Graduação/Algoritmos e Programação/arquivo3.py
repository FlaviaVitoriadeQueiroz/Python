with open("B:/VScode/Python/ap/vendas.csv", "a+", encoding="utf-8") as arquivo:
    arquivo.write("Pascal\n")          # escreve no finaL
    arquivo.seek(0)                    # move o ponteiro para o início
    for linha in arquivo:
        print(linha.strip())          # lê e imprime todas as linhas

''''r+' → leitura e escrita, sem apagar o conteúdo existente.
'w+' → leitura e escrita, mas apaga o conteúdo ao abrir.
'a+' → leitura e escrita, mas só escreve no final do arquivo.'''

'''"B:/VScode/Python/ap/vendas.csv" e um caminho absoluto e deve ser evitado, pela quantidade de caracteres, e pq as barras mudam para diferentes sitemas operacionais.
Em vez de usar ele pode se usar os.path.join()'''