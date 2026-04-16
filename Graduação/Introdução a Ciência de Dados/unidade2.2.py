import numpy as np
import pandas as pd 

# Para começar a limpeza
info() # Retorna um resumo conciso do DataFrame, incluindo o número de entradas, colunas, tipos de dados e uso de memória, ajudando a identificar possíveis problemas nos dados.
describe() # Retorna estatísticas descritivas para colunas numéricas, incluindo contagem de valores, média, desvio padrão, valores mínimo e máximo, e os quartis, ajudando a entender a distribuição dos dados e identificar possíveis problemas como outliers ou dados faltantes.
value_counts() # Retorna a contagem de valores únicos em uma coluna específica, ajudando a identificar a frequência de cada valor e possíveis inconsistências ou desequilíbrios nos dados.  

# Mas no geral usasse

eda=sv.analyze(dados)
eda.show_html('relatorio_sweetviz.html') 



# Dados faltantes 

# Dados faltantes como identificar
df.isnull() # Retorna um DataFrame booleano indicando onde os valores são nulos, onde True indica um valor nulo e False indica um valor não nulo
df.isnull().sum() # Retorna a contagem de valores nulos por coluna

# Dados faltantes se resolvem com 
df.dropna() # Remove linhas com valores nulos
df.fillna(valor) # Preenche valores nulos com um valor específico

# Para df.fillna() podemos usar a média e mediana para dados numéricos ou moda para dados categóricos
df["coluna"].fillna(df["coluna"].mean(), inplace=True) # Preenche valores nulos na coluna "coluna" com a média da coluna
df["coluna"].fillna(df["coluna"].median(), inplace=True) # Preenche valores nulos na coluna "coluna" com a mediana da coluna
df["coluna"].fillna(df["coluna"].mode()[0], inplace=True) # Preenche valores nulos na coluna "coluna" com a moda da coluna
''' a estrutura ddo codigo é df pois é o nome do dataframe,
"coluna" é o nome da coluna que queremos preencher os valores nulos,
e o valor dentro do fillna() é a média, mediana ou moda da coluna, dependendo do tipo de dado.
O parâmetro inplace=True é usado para modificar o dataframe original sem precisar atribuir o resultado a uma nova variável.'''



# Dados duplicados 

# Dados duplicados como identificar
df.duplicated() # Retorna um Series booleano indicando onde os valores são duplicados, onde True indica uma linha duplicada e False indica uma linha única
df.duplicated().sum() # Retorna a contagem de linhas duplicadas no DataFrame

# Dados duplicados se resolvem com
df.drop_duplicates() # Remove linhas duplicadas do DataFrame



# Dados inconsistentes
# Dados inconsistentes como identificar
df["coluna"].unique() # Retorna os valores únicos presentes na coluna "coluna", permitindo identificar possíveis inconsistências nos dados, como variações de formatação ou erros de digitação.

# Dados inconsistentes se resolvem com
df["coluna"] = df["coluna"].str.lower().str.strip() # Padroniza os valores da coluna "coluna" convertendo para minúsculas e removendo espaços extras, ajudando a resolver inconsistências de formatação nos dados.
df["coluna"] = df["coluna"].replace("valor_inconsistente", "valor_correto") # Substitui um valor inconsistente específico por um valor correto na coluna "coluna", ajudando a resolver inconsistências nos dados.     
df['coluna'].str.replace('valor_inconsistente', 'valor_correto', regex=True) # Substitui um valor inconsistente específico por um valor correto na coluna "coluna" usando expressões regulares, ajudando a resolver inconsistências nos dados.
df['coluna'].str.strip() # Remove espaços extras no início e no final dos valores da coluna "coluna", ajudando a resolver inconsistências de formatação nos dados.
str.func() # Aplica uma função de string a cada valor da coluna "coluna", permitindo realizar transformações personalizadas para resolver inconsistências nos dados.


# Dados Casting

# Dados Casting como identificar
df.dtypes # Retorna os tipos de dados de cada coluna no DataFrame, permitindo identificar possíveis inconsistências de tipo de dados.

3 # Dados Casting se resolvem com
df['coluna'] = df['coluna'].astype(float) # Converte a coluna "coluna" para o tipo float, ajudando a resolver inconsistências de tipo de dados.
df['coluna'] = pd.to_numeric(df['coluna'], errors='coerce') # Converte a coluna "coluna" para o tipo numérico, e se houver valores que não puderem ser convertidos, eles serão definidos como NaN, ajudando a resolver inconsistências de tipo de dados.\  
df['coluna'] = pd.to_datetime(df['coluna'], errors='coerce') # Converte a coluna "coluna" para o tipo datetime, e se houver valores que não puderem ser convertidos, eles serão definidos como NaT (Not a Time), ajudando a resolver inconsistências de tipo de dados.  



# Outliers 

# Como identificar outliers
df.boxplot(column='coluna') # Cria um boxplot para a coluna "coluna", permitindo visualizar a distribuição dos dados e identificar possíveis outliers.
df['coluna'].describe()
# Retorna estatísticas descritivas da coluna "coluna", incluindo o valor mínimo, primeiro quartil, mediana, terceiro quartil e valor máximo, ajudando a identificar possíveis outliers com base nos limites interquartis.

# Como resolver outliers
df = df[df['coluna'] < limite_superior] # Remove linhas onde os valores da coluna "coluna" são maiores que um limite superior definido, ajudando a resolver outliers.
df = df[df['coluna'] > limite_inferior] # Remove linhas onde os valores da coluna "coluna" são menores que um limite inferior definido, ajudando a resolver outliers.
df['coluna'] = np.where(df['coluna'] > limite_superior, limite_superior, df['coluna']) # Substitui valores da coluna "coluna" que são maiores que um limite superior definido pelo próprio limite superior, ajudando a resolver outliers.
df['coluna'] = np.where(df['coluna'] < limite_inferior, limite_inferior, df['coluna']) # Substitui valores da coluna "coluna" que são menores que um limite inferior definido pelo próprio limite inferior, ajudando a resolver outliers.       

