'''airflow  é uma plataforma de código aberto para criar, agendar e monitorar fluxos de trabalho programados.
 Ele é amplamente utilizado para orquestrar tarefas complexas em ambientes de dados,
   permitindo que os usuários definam dependências entre tarefas, agendem execuções e monitorem o progresso das tarefas.
'''

'''o que é um DAG (Directed Acyclic Graph) no Airflow?
Um DAG (Directed Acyclic Graph) no Airflow é uma estrutura de dados que representa um fluxo de trabalho ou pipeline de tarefas.
 Ele é composto por nós (tarefas) e arestas (dependências entre as tarefas). O termo "Directed" indica que as arestas têm uma direção,
 ou seja, uma tarefa depende de outra. O termo "Acyclic" significa que não há ciclos no grafo, ou seja, uma tarefa não pode depender de si mesma direta ou indiretamente. '''


from airflow import DAG
from airflow.operators.python import PythonOperator

dag = DAG(dag_id='sample', start_date=datetime(2023, 1, 1), schedule_interval='0 0 * * *')
 # Define o DAG com um ID, data de início e intervalo de agendamento (neste caso, diariamente à meia-noite)

# parametros padrão 
etl_task = PythonOperator(
    task_id='etl_task', 
    python_callable=etl,
    dag=dag
)

# define a tarefa ETL usando o operador PythonOperator, que executa a função etl definida anteriormente. O task_id é um identificador único para a tarefa dentro do DAG.
etl_task.setupstream("etl_task_stream")