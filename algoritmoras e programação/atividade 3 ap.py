def calcular_viagem():
    tempo = int(input('Digite o tempo em horas: '))
    velocidade = float(input('Digite a velocidade média (km/h): '))
    distancia = velocidade * tempo
    quantidade_de_combustivel = distancia / 1 
    print("A quantidade de combustível utilizada foi de:", quantidade_de_combustivel)

calcular_viagem()
