'''Erros do código:
1. Não foi feita a divisão dos dados em treino e teste, o que é fundamental para avaliar o desempenho do modelo de forma justa.
2. Não foi feita a normalização dos dados, o que pode afetar o desempenho do modelo KNN, pois ele é baseado na distância entre os pontos.
3. O modelo foi avaliado usando os mesmos dados de treino, o que pode levar a uma avaliação otimista do desempenho do modelo. É importante usar dados de teste separados para avaliar o modelo de forma justa.
4. Não foi feita a previsão para uma nova flor, o que é uma parte importante do processo de ML, pois queremos que o modelo seja capaz de fazer previsões para novos dados.'''

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier 
from sklearn import datasets
import seaborn as sns


iris = datasets.load_iris()

# Load the dataset and create a DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target #adicionando a coluna 'species' com os valores da variável target do dataset iris

# Determinando as features
iris_features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

# Determinando o alvo
y = df['species']

'''Em ML normalmente os dados s'ao X maiusculo e o alvo é y minusculo, mas isso é apenas uma convenção. O importante é entender que X são as features e y é o alvo.'''

X  = df [iris_features]

''' Define = escolhe o modelo de ML que vamos usar, nesse caso o KNN.
Fit = treina o modelo com os dados de treino.
Predict = faz as previsões com os dados de teste.
Evaluate = avalia o desempenho do modelo com as previsões feitas.'''

# Criando o modelo KNN
modelo = KNeighborsClassifier(3) #criando o modelo KNN com k=5, ou seja, o modelo vai considerar os 5 vizinhos mais próximos para fazer a classificação

# Treinando o modelo
modelo.fit(X, y) #treinando o modelo com os dados de treino (X e y)

# Ver a predição do modelo
print(modelo.predict(X)) #fazendo as previsões com os dados de teste (X) e mostrando as previsões feitas pelo modelo

# Vamos avaliar o modelo
print(modelo.score(X, y)) #avaliando o desempenho do modelo com os dados de teste (X e y) e mostrando a acurácia do modelo

