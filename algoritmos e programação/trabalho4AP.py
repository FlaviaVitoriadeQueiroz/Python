n = int(input("Digite um número natural qualquer (inteiro e positivo):"))
def somar(n):
    if n == 0:
        return 0
    return n + somar(n - 1)

print(f"A soma de todos os numeros de {n} ate 0 e {somar(n)}")