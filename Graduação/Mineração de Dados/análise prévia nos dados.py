import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\\Users\\F Vitória de Queiroz\Downloads\\pokemon.csv")

# Informações gerais
print(df.info())

# Valores nulos
print(df.isnull().sum())

# Percentual de valores nulos
missing_percent = df.isnull().mean() * 100
print(missing_percent)

# Contar valores - dentro da coluna 'Type 2', o valor '-' indica que o pokémon não tem um segundo tipo
qtd_traco = (df['Type 2'] == '-').sum()
print("Quantidade de '-' em Type 2:", qtd_traco)


# Visualização de valores nulos
df['Type 2'] = df['Type 2'].replace('-', pd.NA)
sns.heatmap(df.isnull(), cbar=False) #cor clara para valores nulos e escura para valores preenchidos
plt.title("Mapa de Valores '-' na coluna 'Type 2' ")
plt.show()

