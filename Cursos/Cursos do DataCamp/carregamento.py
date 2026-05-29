'''oltp - online transaction processing
olap - online analytical processing
mpp - massively parallel processing'''

'''exemplos de mpp: snowflake, amazon redshift, google bigquery, databricks, azure sql data warehouse'''

'''exemplos de oltp: mysql, postgresql, sql server, oracle, ibm, amazon, mongodb, redis'''

'''exemplos de olap: snowflake, amazon redshift, google bigquery, databricks, azure sql data warehouse'''

'''bancos mpp carregam melhor dados de arquivos do que de bancos relacionais
o formato do arquivo é importante, o parquet é um formato colunar otimizado para leitura e escrita de grandes volumes de dados'''

# tem como escrever esse tipo de arquivo com pandas
df.to_parquet('dados.parquet')

# tem como escrever com pyspark
df.write.parquet('dados.parquet')

# tem como escrever com polars
df.write.parquet('dados.parquet')


# depois disso você pode se conectar ao redshift, bigquery, snowflake, databricks ou azure sql data warehouse usando um url

'''COPY customer 
FROM 's3://mybucket/data/customer.csv'
FORMAT as parquet'''