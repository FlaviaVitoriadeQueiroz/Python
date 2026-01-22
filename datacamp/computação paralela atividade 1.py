@print_timing # Decorador para medir o tempo de execução de funções
def parallel_apply(apply_func, groups, nb_cores): # Função para aplicar uma função em paralelo usando multiprocessing
    with Pool(nb_cores) as p: # Cria um pool de processos com o número especificado de núcleos
        results = p.map(apply_func, groups) # Aplica a função em paralelo para cada grupo
    return pd.concat(results) # Concatena os resultados em um único DataFrame


parallel_apply(take_mean_age, athlete_events.groupby('Year'), 1) # Chama a função parallel_apply com 1 núcleo


parallel_apply(take_mean_age, athlete_events.groupby('Year'), 2)


parallel_apply(take_mean_age, athlete_events.groupby('Year'), 4)

#Foi usado api de baixo nível do multiprocessing para demonstrar como a computação paralela pode ser implementada manualmente em Python.
#No entanto, essa abordagem é mais complexa e menos eficiente do que usar bibliotecas como Dask, que abstraem muitos dos detalhes da computação paralela e otimizam o desempenho automaticamente.

#Um multiprocessing Pool é uma coleção de processos que podem ser usados para executar tarefas em paralelo. Ele gerencia a criação, distribuição de tarefas e coleta de resultados dos processos filhos, 
#facilitando a execução paralela de funções em múltiplos núcleos da CPU.