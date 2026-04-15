import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv(r"C:\\Users\\F Vitória de Queiroz\Downloads\\pokemon.csv")  

# Visão geral
print("Primeiras linhas:")
print(df.head())

print("\nÚltimas linhas:")
print(df.tail())

print("\nFormato do dataset:")
print(df.shape)

print("\nColunas:")
print(df.columns)

# Informações gerais
print("\nInformações:")
print(df.info())

print("\nEstatísticas descritivas:")
print(df.describe())

# Valores nulos
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# Histogramas
df.hist(figsize=(10, 8))
plt.suptitle("Distribuição dos Dados")
plt.show()

# Mapa de correlação
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Mapa de Correlação")
plt.show()

# Boxplot (outliers)
plt.figure(figsize=(10, 6))
sns.boxplot(data=df)
plt.xticks(rotation=90)
plt.title("Detecção de Outliers")
plt.show()

# Scatter plot (troque pelos nomes das colunas)
# Exemplo:
# sns.scatterplot(x="idade", y="salario", data=df)
# plt.show()

# Gráfico de contagem (categorias)
# Exemplo:
# sns.countplot(x="sexo", data=df)
# plt.show()

# Pairplot (visualização geral)
sns.pairplot(df)
plt.show()