import pandas as pd



# Etapa 1 do KDD: Data Cleaning (Limpeza de Dados)

df = pd.read_csv("dados.csv")

# Remover linhas com valores nulos
df = df.dropna()



# Etapa 2 do KDD: Data Integration (Integração de Dados)

#Trata dados ausentes 
#Calcula a média da coluna idade sem o outlier
media_idade = df[df["idade"] < 100]["idade"].mean() # Calcula a média da coluna "idade" apenas para os valores menores que 100, ignorando possíveis outliers
df["idade"] = df["idade"].fillna(media_idade) # Preenche os

# Tratar dados ausentes
df["salario"] = df["salario"].fillna(df["salario"].mean()) # Preenche valores ausentes na coluna "salario" com a média da coluna


# Remover duplicatas
df = df.drop_duplicates()


# Tratar outliers
df = df[df["salario"] < 10000] # Remove linhas onde o salário é maior que 10000

# Padronizar texto
df["nome"] = df["nome"].str.lower().str.strip() # Converte para minúsculas e remove espaços extras


# Corrige tipos de dados
df["data"] = pd.to_datetime(df["data"]) # Converte a coluna "data" para o tipo datetime
df["preco"] = df["preco"].astype(float) # Converte a coluna "preco" para o tipo float



# Etapa 3 do KDD: Data Transformation (Transformação de Dados)

# Criar atributos derivados
df["idade_categoria"] = pd.cut(df["idade"], bins=[0, 18, 35, 60, 100], labels=["Criança", "Jovem", "Adulto", "Idoso"]) # Cria uma nova coluna "idade_categoria" categorizando a idade em faixas 

# Normalizar dados
df["salario_normalizado"] = (df["salario"] - df["salario"].min()) / (df["salario"].max() - df["salario"].min()) # Normaliza a coluna "salario" usando a fórmula de normalização min-max     

