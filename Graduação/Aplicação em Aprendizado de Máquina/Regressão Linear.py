'''Antes de começar a codar acredito que seja importante conhecer sobre os dados que serão utilizados, desta forma fiz uma breve pesquisa saobre Abalones

O abalone é um molusco marinho gastrópode (da família Haliotidae) muito apreciado na culinária asiática, conhecido por sua carne firme e sabor suave.

Existem cerca de 50 a 60 espécies de abalone

O dataset contém a parêmetros da biometria 
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn as sk
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error, r2_score  

# Abrindo o arquivo CSV
abalone = pd.read_csv("C:\\Users\\F Vitória de Queiroz\\Downloads\\abalone.csv")

# EDA - Análise Exploratória de Dados
print(f"Primeiras linhas do DataFrame:\n{abalone.head()}")  # Exibindo as primeiras linhas do DataFrame
print(f"Informações sobre o DataFrame:\n{abalone.info()}")  # Exibindo informações sobre o DataFrame
print(f"Estatísticas descritivas do DataFrame:\n{abalone.describe()}")  # Exibindo estatísticas descritivas do DataFrame
print(f"Valores ausentes no DataFrame:\n{abalone.isna().sum()}")  # Verificando se há valores ausentes no DataFrame
print(f"Número de linhas do DataFrame:\n{len(abalone)}")  # Exibindo o número de linhas do DataFrame

# Visualização dos dados

# Defina cores para cada categoria de sexo
cores_sexo = {
    'M': 'blue',
    'F': 'pink',
    'I': 'yellow'
}

# Cria uma coluna com as cores
abalone['cor'] = abalone['Sex'].map(cores_sexo)

# Gráfico de Idade (Rings) vs Comprimento (Length)
plt.figure(figsize=(10, 6))
sns.scatterplot( # scatterplot é um gráfico de dispersão, onde cada ponto representa uma observação do dataset, e a posição do ponto é determinada pelos valores das variáveis 'Length' e 'Rings'. O parâmetro 'hue' é usado para colorir os pontos com base na variável
    data=abalone,
    x='Length',
    y='Rings',
    hue='Sex', # O parâmetro 'hue' é usado para colorir os pontos com base
    palette={'M':'blue', 'F':'pink', 'I':'yellow'}, # O parâmetro 'palette' é usado para definir as cores específicas para cada categoria de sexo ('M', 'F', 'I') no gráfico de dispersão. Neste caso, os pontos correspondentes a 'M' serão azuis, os pontos correspondentes a 'F' serão rosa e os pontos correspondentes a 'I' serão amarelos.
    alpha=0.5
)
plt.title('Rings vs Length')
plt.show()

# Gráfico de Comprimento (Length) vs Peso Total (Whole weight)
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=abalone,
    x='Length',
    y='Whole weight',
    hue='Sex',
    palette={'M':'blue', 'F':'pink', 'I':'yellow'},
    alpha=0.5
)
plt.title('Whole weight vs Length')
plt.show()

# Gráfico de Altura (Height) vs Peso Sem Casca (Shucked weight)
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=abalone,
    x='Height',
    y='Shucked weight',
    hue='Sex',
    palette={'M':'blue', 'F':'pink', 'I':'yellow'},
    alpha=0.5
)
plt.title('Shucked weight vs Height')
plt.show()

# Histograma da distribuição dos anêis (Rings) 
sns.histplot(
    data=abalone,
    x='Length',
    hue='Sex',
    palette={'M':'blue', 'F':'pink', 'I':'yellow'},
    multiple='stack'
)
plt.title('Distribuição de Length por Sex')
plt.show()


# Usando modelo de regressão linear para prever a idade (Rings)

# Selecionando as variáveis independentes (X) e a variável dependente (y)
X = abalone[['Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight']]
y = abalone['Rings']

# Configurando o K-Fold
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Listas para armazenar as métricas
'''rsme_score é a raiz do erro quadrático médio, que é uma medida de quão bem o modelo de regressão linear está se ajustando aos dados. 
Ele é calculado como a raiz quadrada da média dos erros quadráticos entre as previsões do modelo e os valores reais. 
Quanto menor o RMSE, melhor o modelo está se ajustando aos dados.

r2_score é o coeficiente de determinação, que é uma medida de quão bem as previsões do modelo se ajustam aos dados.
Ele varia entre 0 e 1, onde um valor mais próximo de 1 indica um melhor ajuste do modelo aos dados. 
O R² é calculado como 1 menos a razão entre a soma dos quadrados dos resíduos (diferença entre as previsões do modelo e os valores reais) e
 a soma dos quadrados totais (diferença entre os valores reais e a média dos valores reais).
'''

rmse_scores = []
r2_scores = []

for fold, (train_idx, test_idx) in enumerate(kf.split(X), start=1):

    X_train = X.iloc[train_idx]
    X_test = X.iloc[test_idx]

    y_train = y.iloc[train_idx]
    y_test = y.iloc[test_idx]

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    rmse_scores.append(rmse)
    r2_scores.append(r2)

    print(f"Fold {fold}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R²: {r2:.4f}")
    print("-" * 30)

print("\nResultado Médio dos 5 Folds")
print(f"RMSE Médio: {np.mean(rmse_scores):.4f}")
print(f"R² Médio: {np.mean(r2_scores):.4f}")