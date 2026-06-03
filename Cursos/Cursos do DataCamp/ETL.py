'''' esse código é um exemplo de um processo ETL (Extract, Transform, Load) usando Python e pandas. 
Ele extrai dados de uma tabela em um banco de dados, transforma os dados dividindo uma coluna em duas novas colunas, 
e depois carrega os dados transformados de volta para o banco de dados. '''

def extract_table_to_df(tablename, db_engine):
    return pd.read_sql(f"SELECT * FROM {tablename}", db_engine)

def split_columns(df, column_to_split, new_column_names, separator):
    new_columns = df[column_to_split].str.split(separator, expand=True)
    new_columns.columns = new_column_names
    return pd.concat([df.drop(columns=[column_to_split]), new_columns], axis=1)

def load_df_into_dwh(df, tablename, db_engine):
    return pd.to_sql(tablename, db_engine, if_exists='replace', index=False)

db_engine = create_engine('postgresql://user:password@localhost:5432/mydatabase')
def etl():
    df = extract_table_to_df('my_table', db_engine)
    df = split_columns(df, 'full_name', ['first_name', 'last_name'], ' ')
    load_df_into_dwh(df, 'my_table_transformed', db_engine)