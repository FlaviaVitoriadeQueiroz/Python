import pandas as pd


# Lendo dados de diferentes fontes
pd.read_csv()
pd.read_excel()
pd.read_sql()
pd.read_json()


# Transformando o arquivo em um DataFrame
df = pd.read_csv('dados_vendas.csv')


# Algumas funções básicas para explorar os dados
df.head() # Exibe as primeiras linhas do DataFrame
df.info() # Exibe informações sobre o DataFrame, como tipos de dados e valores n
df.shape() # Exibe o número de linhas e colunas do DataFrame
df.describe() # Exibe estatísticas descritivas para colunas numéricas
# describe() retorna contagem, média, desvio padrão, valores mínimo e máximo, e os quartis (25%, 50% e 75%).
# describe() é útil para obter uma visão geral dos dados numéricos, identificar possíveis outliers e entender a distribuição dos dados.


# Seleção e Indexação
df.loc[] #Seleciona dados por rótulo
#exemplo: df.loc[1, Nome] seleciona o valor da coluna 'Nome' na segunda linha

df.iloc[] # Seleciona dados por posição
# exemplo: df.iloc[1, 0] seleciona o valor da primeira coluna na segunda linha
# 0 é a segunda linha, pois a indexação começa em 0

# Filtragem Condicional
# Sintaxe: df[condição]
# Exemplo:
vendas_altas = df[df['Valor'] > 1000]
# vendas_altas é um DataFrame que contém apenas as linhas onde o valor da coluna 'Valor' é maior que 1000
# df[df['Valor'] > 1000] retorna um DataFrame filtrado com as linhas que atendem à condição

mulheres_ti = df[(df['Sexo']=='F') & (df['Area']=='TI')]
# mulheres_ti é um DataFrame que contém apenas as linhas onde a coluna 'Sexo' é igual a 'F' e a coluna 'Area' é igual a 'TI'
# df[(df['Sexo']=='F') & (df['Area']=='TI')] retorna um DataFrame filtrado com as linhas que atendem às duas condições: sexo feminino e área de TI

# Resultado: Cria um novo DataFrame apenas com as linhas que satisfazem a condição.



# Agrupamento (Groupby)
df.groupby('Departamento')['Salario'].mean() # estamos agrupando por departamento e calculando a média salarial para cada departamento
# df.groupby('Departamento')['Salario'].mean() retorna uma série com a média salarial para cada departamento
# O resultado é uma série onde o índice é o nome do departamento e os valores são as médias salariais correspondentes a cada departamento.

# Conceito: Dividir - Aplicar - Combinar (Split-Apply-Combine)
# Objetivo: Calcular estatísticas por categorias
# Equivalente: Tabela Dinâmica (Pivot Table) do Excel.
