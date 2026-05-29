import pyspark.sql 


spark = pyspark.sql.SparkSession.builder.getOrCreate()

# Carregar dados de um banco de dados PostgreSQL
spark.read.jdbc('jdbc:postgresql://localhost:5432/your_database', 'your_table', properties={'user': 'your_username', 'password': 'your_password'})
