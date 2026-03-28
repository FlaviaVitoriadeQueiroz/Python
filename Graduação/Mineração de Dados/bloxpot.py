# Boxplot é uma representação gráfica que mostra a distribuição de um conjunto de dados, destacando a mediana, os quartis e os valores atípicos. 
# Ele é útil para identificar a dispersão dos dados e possíveis outliers.

import seaborn as sns
import matplotlib.pyplot as plt

# Dados de exemplo
dados = [10, 20, 15, 30, 45, 50, 60, 5, 100]

sns.boxplot(data=dados)
plt.title("Boxplot com Seaborn")

plt.show()



import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Criando um DataFrame
df = pd.DataFrame({
    "Grupo": ["A", "A", "A", "B", "B", "B"],
    "Valores": [10, 20, 15, 30, 40, 35]
})

sns.boxplot(x="Grupo", y="Valores", data=df)
plt.title("Boxplot por Grupo")

plt.show()



import seaborn as sns
import matplotlib.pyplot as plt

# Dados de exemplo
dados = [10, 20, 15, 30, 45, 50, 60, 5, 100]

sns.boxplot(data=dados)
plt.title("Boxplot com Seaborn")

plt.show()