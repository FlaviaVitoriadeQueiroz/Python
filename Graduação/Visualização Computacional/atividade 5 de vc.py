import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import kagglehub
import os

# Baixar dataset do Kaggle
path = kagglehub.dataset_download("nelgiriyewithana/top-spotify-songs-2023")

# Mostrar caminho do dataset
print("Path to dataset files:", path)

# Mostrar arquivos disponíveis
print(os.listdir(path))

# Ler o arquivo CSV com encoding correto
df = pd.read_csv(
    f"{path}/spotify-2023.csv",
    encoding="latin1"
)

# Mostrar primeiras linhas
print(df.head())

# Remover linhas com valores vazios
df = df.dropna()
print("\nLinhas com valores vazios removidas!")


# Exibir estatísticas descritivas para colunas numéricas
print("\nESTATÍSTICAS DESCRITIVAS:")

# Selecionar apenas colunas numéricas
numericas = df.select_dtypes(include=np.number)

# Média
print("\nMÉDIA:")
print(numericas.mean())

# Mediana
print("\nMEDIANA:")
print(numericas.median())

# Desvio padrão
print("\nDESVIO PADRÃO:")
print(numericas.std())

# Valor mínimo
print("\nVALOR MÍNIMO:")
print(numericas.min())

# Valor máximo
print("\nVALOR MÁXIMO:")
print(numericas.max())

# Resumo estatístico completo

print("\nRESUMO ESTATÍSTICO:")
print(numericas.describe())


# Exemplo de visualização 1
# Top 10 artistas mais frequentes

top_artists = df["artist(s)_name"].value_counts().head(10)

plt.figure(figsize=(10, 5))

top_artists.plot(kind="bar")

plt.title("Top 10 Artistas Mais Frequentes")
plt.xlabel("Artista")
plt.ylabel("Quantidade de Músicas")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# Exemplo de visualização 2
# Distribuição de energia das músicas

plt.figure(figsize=(8, 5))

sns.histplot(df["energy_%"], bins=20)

plt.title("Distribuição de Energia das Músicas")
plt.xlabel("Energy %")
plt.ylabel("Quantidade")

plt.tight_layout()
plt.show()