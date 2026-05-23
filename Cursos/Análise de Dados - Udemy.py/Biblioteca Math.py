import math 

def calcular_area_circulo(raio):
    area = math.pi * raio ** 2
    return area 

def calcular_hipotenusa(cateto1, cateto2):
    hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
    return hipotenusa

def calcular_logaritmo(numero, base=math.e):
    logaritmo = math.log(numero, base)
    return logaritmo

def calcular_fatorial(numero):
    fatorial = math.factorial(numero)
    return fatorial

def calcular_seno(angulo):
    seno = math.sin(math.radians(angulo))
    return seno

def calcular_cosseno(angulo):
    cosseno = math.cos(math.radians(angulo))
    return cosseno

def calcular_tangente(angulo):
    tangente = math.tan(math.radians(angulo))
    return tangente


math.sqrt(16)  # Raiz quadrada de 16

math.ceil(3.7)  # Arredonda para cima

math.floor(3.7)  # Arredonda para baixo

pow(2, 3)  # 2 elevado à potência de 3

abs(-5)  # Valor absoluto de -5

tupla = (1, 2, 3, 4, 5)
maximo = max(tupla)  # Valor máximo da tupla    
minimo = min(tupla)  # Valor mínimo da tupla
