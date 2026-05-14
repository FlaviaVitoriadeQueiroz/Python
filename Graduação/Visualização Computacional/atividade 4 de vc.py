
import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
df = pd.read_csv("train.csv")

# Print dos dados para verificar a estrutura
print(df.head())

# Remover linhas com valores faltantes
df = df.dropna()

# Print dos dados após remoção de valores faltantes
print(df.head())

# Gráfico 1: Distribuição da classe dos passageiros por sobrevivência

pclass_survived = pd.crosstab(df["Pclass"], df["Survived"])
pclass_survived.columns = ["Não Sobreviveu", "Sobreviveu"]
pclass_survived.plot(kind="bar")

plt.title("Distribuição da Classe dos Passageiros por Sobrevivência")
plt.xlabel("Classe do Passageiro (Pclass)")
plt.ylabel("Quantidade")
plt.xticks(rotation=0)
plt.legend(title="Situação")

plt.show()


# Gráfico 2: Distribuição de sexo por sobrevivência

sex_survived = pd.crosstab(df["Sex"], df["Survived"])
sex_survived.columns = ["Não Sobreviveu", "Sobreviveu"]
sex_survived.plot(kind="bar")

plt.title("Distribuição de Sexo por Sobrevivência")
plt.xlabel("Sexo")
plt.ylabel("Quantidade")
plt.xticks(rotation=0)
plt.legend(title="Situação")

plt.show()
