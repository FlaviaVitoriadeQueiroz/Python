with open("B:\\VScode\\Python\\ap\\vendas.csv", "a", encoding="utf-8") as arquivo:
    arquivo.write("Pascal\n")

with open("B:/VScode/Python/ap/vendas.csv", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())