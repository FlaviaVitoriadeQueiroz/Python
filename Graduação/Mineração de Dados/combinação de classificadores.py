# ATIVIDADE - COMBINAÇÃO DE CLASSIFICADORES
# Técnica utilizada: Random Forest
# Biblioteca: scikit-learn


# Importação das bibliotecas
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# CARREGAMENTO DO DATASET
# Carrega a base Iris
iris = load_iris()

# Variáveis de entrada (atributos)
X = iris.data

# Variável alvo (classes)
y = iris.target

# DIVISÃO DOS DADOS
# Divide os dados em treino e teste
# 70% treino e 30% teste
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# CRIAÇÃO DO MODELO
# Random Forest = combinação de várias árvores de decisão
modelo = RandomForestClassifier(
    n_estimators=100,   # quantidade de árvores
    random_state=42
)

# Treinamento do modelo
modelo.fit(X_train, y_train)

# REALIZAÇÃO DAS PREVISÕES
# Faz previsões com os dados de teste
y_pred = modelo.predict(X_test)

# AVALIAÇÃO DO MODELO
# Calcula a acurácia
acuracia = accuracy_score(y_test, y_pred)

print("Acurácia do modelo:", acuracia)

# Relatório de classificação
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

# Matriz de confusão
print("\nMatriz de Confusão:")
print(confusion_matrix(y_test, y_pred))