def load(data_frame, target_table):
    # Função para carregar dados em uma tabela de banco de dados PostgreSQL
    data_frame.to_sql(name=target_table, con=POSTGRES_CONNECTION)
    print(f"Loading de dados na tabela {target_table} concluída.")

extracted_data = extract(file_name="raw_data.csv")
transforme_data = transform(data_frame=extracted_data)
load(data_frame=transforme_data, target_table="dados_limpos")