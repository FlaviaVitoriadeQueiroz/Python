'''Esse pacote tem como objetivo criar funções para calcular as principais medidas de tendência central e de dispersão.'''

import statistics

# Sem a biblioteca statistics, podemos criar nossas próprias funções para calcular as medidas de tendência central e de dispersão:
Lista = [10, 20, 30, 40, 50]

def calcular_media(lista):
    media = sum(lista) / len(lista)
    return media

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 0:
        mediana = (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    else:
        mediana = lista_ordenada[n // 2]
    return mediana  

def calcular_moda(lista):
    from collections import Counter
    contagem = Counter(lista)
    moda = contagem.most_common(1)[0][0]
    return moda

def calcular_variancia(lista):
    media = calcular_media(lista)
    variancia = sum((x - media) ** 2 for x in lista) / len(lista)
    return variancia

def calcular_desvio_padrao(lista):
    variancia = calcular_variancia(lista)
    desvio_padrao = variancia ** 0.5
    return desvio_padrao

# Com a biblioteca statistics, podemos calcular as medidas de tendência central e de dispersão de forma mais simples:

statistics.variance(Lista)  # Variância da lista
statistics.stdev(Lista)     # Desvio padrão da lista    
statistics.mean(Lista)     # Média da lista
statistics.median(Lista)   # Mediana da lista
statistics.mode(Lista)     # Moda da lista

