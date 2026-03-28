import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\F Vitória de Queiroz\Downloads\pokemon.csv")

# Ordenar tipos pela mediana de BST
ordem = df.groupby("Type 1")["BST"].median().sort_values().index

plt.figure(figsize=(14,6))

sns.boxplot(
    x="Type 1",
    y="BST",
    data=df,
    order=ordem
)

plt.title("Distribuição de BST por Tipo de Pokémon")
plt.xlabel("Tipo")
plt.ylabel("BST")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()