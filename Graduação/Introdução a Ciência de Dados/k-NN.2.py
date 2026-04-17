import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score


# Load the dataset
df = sns.load_dataset('iris')


# EDA
print("--- PRIMEIRAS LINHAS DO DATASET ---")
print(df.head())


# Vendo quantas flores de cada tipo temos
print("\n--- CONTAGEM DE CADA CLASSE ---")
print(df['species'].value_counts())


# Visualização
'''sns.scatterplot (data=df, x='petal_length', y='petal_width', hue='species') #hue para colorir os pontos de acordo com a espécie 
plt.title('Distribuição das Flores por Comprimento e Largura da Pétala')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()'''


# Dados de treino e teste
'''Dados de treino e teste são usados para avaliar o desempenho do modelo.
O modelo é treinado com os dados de treino e depois testado com os dados de teste para verificar sua capacidade de generalização.

Dados de treino: usados para ajustar os parâmetros do modelo. E são 70% dos dados originais.
Dados de teste: usados para avaliar o desempenho do modelo. E são 30% dos dados originais.'''


# Separando as perguntas (x) das respostas (y)
x = df.drop(columns='species') #todas as colunas menos a coluna 'species'
y = df['species']


# Dividindo os dados em treino e teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42) #test_size para definir a proporção de dados de teste, random_state para garantir a reprodutibilidade igual a 42


'''É preciso normalizar os dados para que o modelo KNN funcione corretamente, pois ele é baseado na distância entre os pontos.
Se os dados não forem normalizados, as características com valores maiores podem dominar a distância e afetar'''

# Normalização dos dados
scaler = MinMaxScaler() #padronizando para uma escala de 0 a 1
x_train = scaler.fit_transform(x_train) #ajustando o scaler aos dados de treino e transformando os dados de treino
x_test = scaler.transform(x_test) #transformando os dados de teste usando o mesmo scaler

print("\n--- DADOS NORMALIZADOS ---")
print("Dados de Treino:\n", x_train[:5]) #mostrando as primeiras 5 linhas dos dados de treino normalizados
print("\nDados de Teste:\n", x_test[:5]) #mostrando as primeiras 5 linhas dos dados de teste normalizados   


# Criando o modelo KNN
knn = KNeighborsClassifier(n_neighbors=5) #criando o modelo KNN com k=5

# Treinando o modelo
knn.fit(x_train, y_train) #ajustando o modelo aos dados de treino

print("Modelo treinado com sucesso!")


# Hora de fazer as previsões
previsoes = knn.predict(x_test) #fazendo as previsões com os dados de teste

# Avaliação do modelo/Medindo a acurácia do modelo
acuracia = accuracy_score(y_test, previsoes) * 100 #calculando a acurácia do modelo
print(f"Acurácia do modelo: {acuracia:.2f}%")

# Simulando uma nova flor para prever sua espécie
nova_flor = [[5.1, 3.5, 1.4, 0.2]] #criando uma nova flor com as características: comprimento da sépala, largura da sépala, comprimento da pétala e largura da pétala
nova_flor_normalizada = scaler.transform(nova_flor) #normalizando a nova flor

previsao_nova_flor = knn.predict(nova_flor_normalizada) #fazendo a previsão para a nova flor
print(f"Previsão para a nova flor: {previsao_nova_flor[0]}")

