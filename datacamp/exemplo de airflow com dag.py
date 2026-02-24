# Create the DAG object
dag = DAG(dag_id="car_factory_simulation",
          default_args={"owner": "airflow","start_date": airflow.utils.dates.days_ago(2)}, # Set the start date to 2 days ago
          schedule_interval="0 * * * *") # Run every hour