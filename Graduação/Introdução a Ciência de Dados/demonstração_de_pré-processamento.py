import pandas as pd

arquivo = 'https://raw.githubusercontent.com/JeffSackmann/tennis_atp/master/atp_matches_2021.csv'
dados = pd.read_csv(arquivo)


# Os comandos a seguir são usados para explorar e pré-processar os dados do DataFrame 'dados', que contém informações sobre partidas de tênis. 
dados.head(5) # Exibe as primeiras 5 linhas do DataFrame, permitindo uma visão geral dos dados e ajudando a identificar possíveis problemas ou padrões nos dados.
dados.info() # Retorna um resumo conciso do DataFram
dados.describe(inclued = 'all')
dados.value_counts() # Conta o número de ocorrências de cada valor único em uma coluna específica, útil para entender a distribuição dos dados e identificar valores comuns ou raros.
dados.isnull()
dados.isnull().sum() 
dados['winner_entry'].describe() # Fornece estatísticas descritivas para a coluna 'winner_entry', como contagem, média, desvio padrão, valores mínimos e máximos, e os quartis. Isso ajuda a entender a distribuição dos dados nessa coluna específica.
dados['winner_entry'].unique() # Retorna os valores únicos presentes na coluna 'winner_entry', permitindo identificar as categorias ou tipos de entradas dos vencedores.


# Os comandos a seguir são usados para lidar com valores nulos (NaN) no DataFrame 'dados', que podem ocorrer quando informações estão ausentes ou não disponíveis.
dados.fillna(0)  # Substitui os valores nulos (NaN) por um valor específico, neste caso, 0. Isso é útil para evitar erros em análises ou modelos que não lidam bem com valores ausentes.
dados.dropna()  # Remove as linhas que contêm valores nulos (NaN)   


# Os comandos a seguir são usados para lidar com valores nulos (NaN) de forma mais específica, dependendo da coluna e do contexto dos dados.
dados.dropna(subset=['loser-rank'], inplace=True) # Remove as linhas que contêm valores nulos (NaN) na coluna 'loser-rank' e atualiza o DataFrame original. Isso é útil para garantir que as análises ou modelos subsequentes não sejam afetados por dados ausentes nessa coluna específica.
dados.dropna(axis=1, how='all') # Remove as colunas que contêm apenas valores nulos (NaN) em todas as linhas. Isso é útil para limpar o DataFrame e eliminar colunas que não fornecem informações úteis.
dados['loser_entry'].unique() # Retorna os valores únicos presentes na coluna 'loser_entry', permitindo identificar as categorias ou tipos de entradas dos perdedores.
dados['loser_entry'].fillna(value= 'X', inplace=True) # Substitui os valores nulos (NaN) na coluna 'loser_entry' por um valor específico, neste caso, 'X', e atualiza o DataFrame original. Isso é útil para lidar com dados ausentes nessa coluna de forma consistente.
dados['loser_entry'].unique() # Retorna os valores únicos presentes na coluna 'loser_entry' após a substituição dos valores nulos, permitindo verificar as categorias ou tipos de entradas dos perdedores atualizados.


# Os comandos a seguir são usados para lidar com valores nulos (NaN) em colunas numéricas, substituindo-os por valores específicos ou estatísticas calculadas a partir dos dados.
dados['w_ace'].unique() # Retorna os valores únicos presentes na coluna 'w_ace', permitindo identificar as diferentes contagens de aces dos vencedores.
dados['loser_ht'].unique() # Retorna os valores únicos presentes na coluna 'loser_ht', permitindo identificar as diferentes alturas dos perdedores.
dados.fillna(value={'w_ace' :0, 'loser_ht':dados['loser_ht'].mean()}, inplace=True) # Substitui os valores nulos (NaN) na coluna 'w_ace' por 0 e na coluna 'loser_ht' pela média dos valores presentes nessa coluna, e atualiza o DataFrame original. Isso é útil para lidar com dados ausentes nessas colunas de forma consistente, mantendo a integridade dos dados.
dados['w_ace'].unique() # Retorna os valores únicos presentes na coluna 'w_ace' após a substituição dos valores nulos, permitindo verificar as diferentes contagens de aces dos vencedores atualizados.
dados['loser_ht'].unique() # Retorna os valores únicos presentes na coluna 'loser_ht' após a substituição dos valores nulos, permitindo verificar as diferentes alturas dos perdedores atualizados.


# Os comandos a seguir são usados para lidar com valores nulos (NaN) em colunas numéricas, utilizando o método de preenchimento 'ffill' (forward fill) para substituir os valores ausentes com a última observação disponível.
dados[ 'minutes' ][1975:1990] # Exibe os valores da coluna 'minutes' para as linhas de índice 1975 a 1990, permitindo analisar a duração dos jogos em um intervalo específico.
dados['minutes'].fillna(method= 'ffill', inplace=True) # Substitui os valores nulos (NaN) pela última observação disponível, e atualiza o DataFrame original. Isso é útil para lidar com dados ausentes nessa coluna de forma consistente.
dados[ 'minutes' ][1975:1990] # Exibe os valores da coluna 'minutes' para as linhas de índice 1975 a 1990 após a substituição dos valores nulos, permitindo verificar a duração dos jogos atualizada nesse intervalo específico.


# Os comandos a seguir são usados para lidar com valores duplicados no DataFrame 'dados', garantindo que cada registro seja único e evitando redundâncias que possam afetar as análises subsequentes.
dados.duplicated()
dados.duplicated().sum()
dados.drop_duplicates(subset=[ 'tournet_name' ], inplace=True) # Remove as linhas duplicadas com base na coluna 'tournet_name' e atualiza o DataFrame original. Isso é útil para garantir que cada torneio seja representado apenas uma vez no conjunto de dados, evitando redundâncias e possíveis distorções nas análises subsequentes.
dados[ 'tourney_name' ].head(10) # Exibe os primeiros 10 valores da coluna 'tourney_name', permitindo verificar os nomes dos torneios presentes no conjunto de dados após a remoção de duplicatas.
dados.describe()



AAPL = https://finance.yahoo.com/quote/AAPL/history/
dados2=pd.read_csv('AAPL.csv')

print(dados2)

# Os comandos a seguir são usados para explorar e pré-processar os dados do DataFrame 'dados2', que contém informações históricas sobre as ações da Apple Inc. (AAPL).
# Criou-se novas colunas para analisar a variação dos preços de fechamento das ações da Apple Inc. ao longo do tempo, permitindo comparar o preço de fechamento de um dia com o dia anterior e calcular a porcentagem de variação entre eles. Além disso, foram removidas as linhas que contêm valores nulos (NaN) na coluna 'allteracao %' para garantir que as análises subsequentes sejam baseadas apenas em dados completos.
dados2[ 'close_ontem' ] = dados2[ 'Close' ].shift(1) # Cria uma nova coluna 'close_ontem' que contém os valores da coluna 'Close' deslocados para baixo em uma posição, permitindo comparar o preço de fechamento de um dia com o dia anterior.

print(dados2)

dados2[ 'allteracao %' ] = ((dados2[ 'Close' ] / dados2 [' close_ontem'])-1)*100 # Cria uma nova coluna 'allteracao %' que calcula a porcentagem de variação entre o preço de fechamento atual e o preço de fechamento do dia anterior, permitindo analisar a volatilidade das ações da Apple Inc. ao longo do tempo.
dados2.head(10) # Exibe as primeiras 10 linhas do DataFrame 'dados2', permitindo uma visão geral dos dados e ajudando a identificar possíveis padrões ou tendências nas variações de preço das ações da Apple Inc.
dados2.dropna(subset=['allteracao %'], inplace=True) # Remove as linhas que contêm valores nulos (NaN) na coluna 'allteracao %' e atualiza o DataFrame original. Isso é útil para garantir que as análises subsequentes sejam baseadas apenas em dados completos e evitar distorções causadas por valores ausentes.

print(dados2)

dados2.describe(include= 'all') # Fornece estatísticas descritivas para todas as colunas do DataFrame 'dados2', incluindo contagem, média, desvio padrão, valores mínimos e máximos, e os quartis. Isso ajuda a entender a distribuição dos dados em todas as colunas, incluindo as variações de preço das ações da Apple Inc.




print(dados['winner_ioc'])
dados['winner_ioc'].unique() # Retorna os valores únicos presentes na coluna 'winner_ioc', permitindo identificar os diferentes países de origem dos vencedores das partidas de tênis.

from sklearn.preprocessing import LabelEncoder # Importa a classe LabelEncoder da biblioteca sklearn.preprocessing, que é usada para converter variáveis categóricas em valores numéricos, facilitando a análise e o uso de algoritmos de machine learning.

paises=dados ['winnwe_ioc']
print(paises)

lencoder = LabelEncoder() # Cria uma instância da classe LabelEncoder, que será usada para transformar os valores categóricos da coluna 'winner_ioc' em valores numéricos. O LabelEncoder atribui um número inteiro único a cada categoria presente na coluna, permitindo que os dados sejam processados por algoritmos de machine learning que exigem entradas numéricas.
paises_numeros = lencoder.fit_transform(paises) # Aplica o método fit_transform do LabelEncoder à coluna 'winner_ioc', que primeiro ajusta o encoder aos dados (fit) e depois transforma os valores categóricos em valores numéricos (transform). O resultado é um array de números inteiros que correspondem às categorias originais da coluna 'winner_ioc', facilitando a análise e o uso de algoritmos de machine learning.
print(paises_numeros)

paises.head(100)

dados [ 'paises_numeros' ] = paises_numeros # Adiciona a nova coluna 'paises_numeros' ao DataFrame 'dados', contendo os valores numéricos correspondentes às categorias originais da coluna 'winner_ioc'. Isso permite que os dados sejam processados por algoritmos de machine learning que exigem entradas numéricas, facilitando a análise e a modelagem dos dados.
print(dados)