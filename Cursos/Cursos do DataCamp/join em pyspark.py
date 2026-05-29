import pyspark.sql 

spark = pyspark.sql.SparkSession.builder.getOrCreate() # Criando uma sessão do Spark

customer_df = spark.read.csv('customer_data.csv', header=True, inferSchema=True) # Carregando um arquivo CSV em um DataFrame do Spark
transaction_df = spark.read.csv('transaction_data.csv', header=True, inferSchema=True) # Carregando um arquivo CSV em um DataFrame do Spark


# avalianado agrupações

ratings_per_costomer = transaction_df.groupBy('customer_id').mean('rating') # Agrupando o DataFrame de transações por 'customer_id' e calculando a média da coluna 'rating' para cada cliente

# fazaendo um join entre os dataframes

customer_df.join(
    ratings_per_costomer, 
    on='customer_id', 
    how='inner'
) # Realizando um join entre o DataFrame de clientes e o DataFrame de avaliações por cliente, usando a coluna 'customer_id' como chave de junção e especificando o tipo de join como 'inner'

# ou

customer_df.join(
    ratings_per_costomer,  
    customer_df.customer_id == ratings_per_costomer.customer_id) # Realizando um join entre o DataFrame de clientes e o DataFrame de avaliações por cliente, usando a condição de igualdade entre as colunas 'customer_id' de ambos os DataFrames como chave de junção