import dask.dataframe as dd

athlete_events_dask = dd.from_pandas(athlete_events, npartitions = 4) # Converte o DataFrame pandas para um DataFrame Dask com 4 partições
result_df = athlete_events_dask.groupby("Year")["Age"].mean().compute() # Agrupa por ano, calcula a média de idade e executa a computação
print(result_df) # Exibe o DataFrame com as médias de idade por ano

#é uma abordagem mais simples e eficiente para computação paralela usando Dask, que gerencia automaticamente a divisão dos dados e a execução paralela.