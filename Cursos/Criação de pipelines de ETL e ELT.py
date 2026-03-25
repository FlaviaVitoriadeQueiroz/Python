import pandas as pd

#impoprtando os dados
data_frame = pd.read_csv("raw_data.csv") #tem outros paramentros que podemos usar, como .head para ver as primeiras linhas, .header para ver os nomes das colunas, e .engine para definir o motor de leitura

#filtrando os dados
#filtrando linhas
data_frame.loc[data_frame["name"] == "Apparel", :] #filtra a coluna name, pegando apenas as linhas que tem o valor "Apparel". : significa todas as colunas
#filtrando colunas
data_frame.loc[:, ["name", "num_firms"]] #pega todas as linhas, mas apenas as colunas name e num_firms

#para carregar todos os arquivos podemos usar .to_csv("nome_arquivo.csv") ou .to_excel("nome_arquivo.xlsx") ou .to_sql("nome_tabela", con=CONEXAO_BANCO_DE_DADOS) ou .to_json("nome_arquivo.json")
data_frame.to_csv("cleaned_data.csv") 

#transformar dados em um warehouse
data_warehouse.execute(
    """
    CREATE TABLE cleaned_data AS #criando uma nova tabela chamada cleaned_data
        SELECT
            name, num_firms
        FROM raw_data
        WHERE name = 'Apparel';
    """
)
#podemos usar um cliente python para executar comandos SQL diretamente no banco de dados, como o SQLAlchemy ou o psycopg2 para PostgreSQL.