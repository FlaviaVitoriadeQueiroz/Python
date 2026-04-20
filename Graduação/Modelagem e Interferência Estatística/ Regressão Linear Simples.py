from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import r2_score

# Dados (X precisa ser 2D)
X = np.array([2, 3, 5, 6, 8]).reshape(-1, 1)  # horas de estudo
y = np.array([5, 6, 7, 8, 9])                # nota

# Criando o modelo
modelo = LinearRegression()

# Treinando o modelo
modelo.fit(X, y)

# Fazendo previsões
y_pred = modelo.predict(X)

# Resultados
print("Coeficiente (inclinação):", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)

# Interpretação simples
print(f"A cada 1 unidade em X, Y varia {modelo.coef_[0]:.2f}")

# Se quiser avaliar o modelo (qualidade)
r2 = r2_score(y, y_pred)
print("R²:", r2)
