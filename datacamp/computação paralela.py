import pandas as pd
from multiprocessing import Pool # Importa a classe Pool para computação paralela

def take_mean_age(year_and_group): # Função para calcular a média de idade por ano
    year, group = year_and_group # declarando as variáveis year e group como os elementos da tupla recebida
    return pd.DataFrame({"Age": group["Age"].mean()}, index=[year]) # Retorna um DataFrame com a média de idade para o ano específico

with Pool(4) as p: # Cria um pool de 4 processos para computação paralela
    results_df = p.map(take_mean_age, athlete_events.groupby("Year")) # Aplica a função take_mean_age em paralelo para cada grupo de anos 
    #map distribui as tarefas entre os processos do pool
    #results armazena os DataFrames retornados por cada chamada da função 
    #athlete_events.groupby("Year") agrupa os dados por ano

mean_ages = pd.concat(results_df) #Concatena os resultados em um único DataFrame
print(mean_ages) #Exibe o DataFrame com as médias de idade por ano
 