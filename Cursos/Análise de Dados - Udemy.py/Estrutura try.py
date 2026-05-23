'''A estrutura try em Python serve para tratar erros sem fazer o programa parar.
Ela é usada quando existe a possibilidade de acontecer algum erro durante a execução.'''


'''# ZeroDivisionError ocorre quando tentamos dividir um número por zero, o que é matematicamente indefinido.
 O IndexError ocorre quando tentamos acessar um índice que está fora do alcance de uma lista ou tupla. 
 O KeyError ocorre quando tentamos acessar uma chave que não existe em um dicionário. O TypeError ocorre quando tentamos realizar uma operação em tipos de dados incompatíveis,
   como somar uma string e um número.'''

try:
    numero = int(input("Digite um número: "))
    print(10 / numero)

except ZeroDivisionError:
    print("Não é possível dividir por zero.")


'''try:
    # código que pode dar erro

except:
    # código executado se houver erro'''


'''ValorError ocorre quando o tipo de dado é incorreto, por exemplo, quando tentamos converter uma string para um número inteiro e a string não contém um número válido. 
O ZeroDivisionError ocorre quando tentamos dividir um número por zero, o que é matematicamente indefinido. 
O IndexError ocorre quando tentamos acessar um índice que está fora do alcance de uma lista ou tupla. 
O KeyError ocorre quando tentamos acessar uma chave que não existe em um dicionário. 
O TypeError ocorre quando tentamos realizar uma operação em tipos de dados incompatíveis, como somar uma string e um número.'''

try:
    numero = int(input("Digite um número: "))

except ValueError:
    print("Digite apenas números.")



# Podemos usar o bloco else para executar um código caso não ocorra nenhum erro:
try:
    numero = int(input("Digite um número: "))   
except ValueError:
    print("Digite apenas números.")
else:
    print("Você digitou o número:", numero)


# Podemos usar o bloco finally para executar um código independentemente de ocorrer um erro ou não:
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Digite apenas números.")
finally:
    print("Esse código será executado independentemente de ocorrer um erro ou não.")


