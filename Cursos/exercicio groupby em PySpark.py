# Print the type of athlete_events_spark
print(type(athlete_events_spark))
#Confirma que você está trabalhando com um DataFrame do PySpark: <class 'pyspark.sql.dataframe.DataFrame'>

# Print the schema of athlete_events_spark
print(athlete_events_spark.printSchema())
#mostra a estrutura do DataFrame, incluindo os nomes das colunas, tipos de dados e se os campos podem ser nulos.
#Um código mais real: athlete_events_spark.printSchema()

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean('Age'))
#apenas descrevre o DataFrame resultante, sem mostrar os dados reais: DataFrame[Year: int, avg(Age): double]
#Porque o Spark é lazy: ele só executa quando você chama uma action.

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean('Age').show())
#show é uma action que força a execução da computação e exibe os resultados.