# Create the DAG object
dag = DAG(dag_id="car_factory_simulation",
          default_args={"owner": "airflow","start_date": airflow.utils.dates.days_ago(2)},
          schedule_interval="0 * * * *")

# Task definitions
assemble_frame = PythonOperator(task_id="assemble_frame", python_callable=lambda: print("Assembling frame"), dag=dag)
place_tires = PythonOperator(task_id="place_tires", python_callable=lambda: print("Placing tires"), dag=dag)
assemble_body = PythonOperator(task_id="assemble_body", python_callable=lambda: print("Assembling body"), dag=dag)
apply_paint = PythonOperator(task_id="apply_paint", python_callable=lambda: print("Applying paint"), dag=dag)

# Complete the downstream flow
assemble_frame.set_downstream(place_tires)
assemble_frame.set_downstream(assemble_body)
assemble_body.set_downstream(apply_paint)