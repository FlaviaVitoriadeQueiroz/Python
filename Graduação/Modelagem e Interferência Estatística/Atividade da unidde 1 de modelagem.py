from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import r2_score 
import matplotlib.pyplot as plt

# Dados (X precisa ser 2D)
X = np.array([25, 50, 75, 100, 120, 150, 175, 200, 225, 250]).reshape(-1, 1)  # massa de fertilizante
y = np.array([84, 80, 90, 154, 148, 169, 206, 244, 212, 248])                 # produção de grama

# Criando o modelo
modelo = LinearRegression()

# Treinando o modelo
modelo.fit(X, y)

# Fazendo previsões
y_pred = modelo.predict(X)

# Resultados
print("Coeficiente:", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)

# Interpretação simples
print(f"A cada 1 unidade em X, Y varia {modelo.coef_[0]:.2f}")

# Se quiser avaliar o modelo (qualidade)
r2 = r2_score(y, y_pred)
print("R²:", r2)

# Gráfico
plt.scatter(X, y, label='Dados Reais')
plt.plot(X, y_pred, color='red', label='Regressão Linear Simples')
plt.xlabel('Massa de Fertilizante')
plt.ylabel('Produção de Grama')
plt.title('O desempenho da produção de grama')
plt.legend()
plt.show()
