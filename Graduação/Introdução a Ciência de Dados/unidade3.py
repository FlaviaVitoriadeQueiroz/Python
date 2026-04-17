# Planejamento e Análise de Resultados 

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, ConfusionMatrixDisplay #importando metricas de avaliação do modelo
from sklearn.model_selection import cross_val_score

# Carregando os dados
dados = load_breast_cancer()
X = dados.data
y = dados.target

# Transformando em DataFrame para facilitar a manipulação
df = pd.DataFrame(X, columns=dados.feature_names)
df['diagnostico'] = y

print(f"Total de exameas: {df.shape[0]}") #mostrando o total de exames, ou seja, o número de linhas do DataFrame
print(f"Total de caracteristicas analisadas por exame: {df.shape[1] - 1}") #subtraindo 1 para não contar a coluna 'diagnostico'
print("\n--- espiando os dados ---")
print(df.head())


# Treinar o modelo KNN
# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) #test_size para definir a proporção de dados de teste, random_state para garantir a reprodutibilidade igual a 42

# Normalzação dos dados
scaler = MinMaxScaler() #padronizando para uma escala de 0 a 1
X_train = scaler.fit_transform(X_train) #ajustando o scaler aos dados de treino e transformando os dados de treino
X_test = scaler.transform(X_test) #transformando os dados de teste usando o mesmo scaler    

# Criando e treinando o modelo KNN
modelo = KNeighborsClassifier(n_neighbors=5) #criando o modelo KNN com k=5, ou seja, o modelo vai considerar os 5 vizinhos mais próximos para fazer a classificação
modelo.fit(X_train, y_train) #treinando o modelo com os dados de treino

# Fazendo previsões e avaliando o modelo
y_pred = modelo.predict(X_test) #fazendo as previsões com os dados de teste
print("\n--- AVALIAÇÃO DO MODELO ---")

# Acurácia
acuracia = accuracy_score(y_test, y_pred)*100 #calculando a acurácia
print(f"Acurácia: {acuracia:.2f}%") 
# A accúracia é de 96.4%

# Como cd de dados é preciso saber onde esáo os erros que passaram 

# Calculando a matriz de confusão
cm = confusion_matrix(y_test, y_pred) #calculando a matriz de confusão

# Desenhando a matriz de confusão
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=dados.target_names) #criando a visualização da matriz de confusão
plt.figure(figsize=(8, 6)) 
disp.plot(cmap= 'Blues') #plotando a matriz de confusão com a paleta de cores 'Blues
plt.title('Matriz de Confusão') 
plt.show() 

'''Disse que 60 casos eram malignos e estava certo
Disse que 105 era belignois e estava certo
Disse que 3 eram malignos e eram belignos
Disse qque 3 eram belignos e eram malignos'''

# Relatório de classificação
print("\n--- RELATÓRIO DE CLASSIFICAÇÃO ---")
print(classification_report(y_test, y_pred, target_names=dados.target_names)) #mostrando o relatório de classificação com as métricas de precisão, recall e f1-score para cada classe

'''--- RELATÓRIO DE CLASSIFICAÇÃO ---
              precision    recall  f1-score   support

   malignant       0.95      0.95      0.95        63
      benign       0.97      0.97      0.97       108

    accuracy                           0.96       171
   macro avg       0.96      0.96      0.96       171
weighted avg       0.96      0.96      0.96       171'''

'''O que podemos entender com esse relatório é que o modelo é melhor em identificar pessoas saúdaveis do que doentes 
'''

# Visualização cruzada 
modelo_cv = KNeighborsClassifier(n_neighbors=5) # cria um novo modelo para testar do 0

# o CV faz todo o processo de dividr, treinar e testar 5 vezes
scores = cross_val_score(modelo_cv, X, y, cv=5, scoring='accuracy') #pegue todos os dados, divida em 5 partes iguais...

print("--- RESULTADO DA VALIDAÇÃO CRUZADA ---")
print(f"Notas das 5 rodadas: {scores}")
print(f"Media Final: {scores.mean() * 100:.2f}%")
print(f"Desvio Padrao: {scores.std():4f}")

'''--- RESULTADO DA VALIDAÇÃO CRUZADA ---
Notas das 5 rodadas: [0.88596491 0.93859649 0.93859649 0.94736842 0.92920354]
Media Final: 92.79%
Desvio Padrao: 0.021763'''
