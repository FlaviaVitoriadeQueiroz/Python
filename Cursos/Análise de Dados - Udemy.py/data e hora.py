import datetime 

# Obter a data e hora atual
data_hora_atual = datetime.datetime.now()

# Exibir a data e hora atual
print("Data e Hora Atual:", data_hora_atual)

# Obter apenas a data atual
data_atual = datetime.date.today()  

# Exibir a data atual
print("Data Atual:", data_atual)

# Obter apenas a hora atual
hora_atual = datetime.datetime.now().time() 

# Exibir a hora atual
print("Hora Atual:", hora_atual)    

# Criar uma coluna de data e hora personalizada
data_hora_personalizada = datetime.datetime(2024, 6, 1, 12, 30, 0)
# Exibir a data e hora personalizada
print("Data e Hora Personalizada:", data_hora_personalizada)



import time

# Obter o tempo atual em segundos desde a época (1 de janeiro de 1970)
tempo_atual = time.time()
print("Tempo Atual (em segundos desde a época):", tempo_atual)

# Obter a data e hora atual usando time
data_hora_atual = time.ctime(tempo_atual)
print("Data e Hora Atual (usando time):", data_hora_atual)

# Obter o tempo atual em formato legível
data_hora_legivel = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(tempo_atual))
print("Data e Hora Atual (formato legível):", data_hora_legivel)

# Time strftime para formatar a data e hora atual
time_texto = '21 June, 2021 14:30:00'
data_hora_formatada = time.strptime(time_texto, "%d %B, %Y %H:%M:%S")
print("Data e Hora Formatada:", time.strftime("%Y-%m-%d %H:%M:%S", data_hora_formatada))

# Time sleep para pausar a execução por um determinado número de segundos
print("Pausando por 3 segundos...") 
time.sleep(3)
print("Continuando...") 

# Time localtime para obter a hora local atual
hora_local = time.localtime()   
print("Hora Local Atual:", time.strftime("%H:%M:%S", hora_local))

# Time gmtime para obter a hora UTC atual
hora_utc = time.gmtime()    
print("Hora UTC Atual:", time.strftime("%H:%M:%S", hora_utc))

# Time perf_counter para medir o tempo de execução de um código
inicio = time.perf_counter()    
# Código a ser medido
for i in range(1000000):
    pass                            

# Time perf_counter para obter o tempo final e calcular o tempo decorrido
fim = time.perf_counter()
tempo_decorrido = fim - inicio
print("Tempo Decorrido para executar o loop:", tempo_decorrido, "segundos") 

