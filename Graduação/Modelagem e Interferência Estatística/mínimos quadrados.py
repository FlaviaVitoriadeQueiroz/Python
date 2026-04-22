import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dados
X = np.array([2, 3, 5, 6, 8]).reshape(-1, 1)
y = np.array([5, 6, 7, 8, 9])

# Modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Previsão (reta)
y_pred = modelo.predict(X)

# Gráfico
plt.scatter(X, y)  # pontos reais
plt.plot(X, y_pred)  # reta da regressão

plt.xlabel("Horas de estudo")
plt.ylabel("Nota")
plt.title("Regressão Linear Simples")
plt.grid(True)

plt.show()

# Parâmetros da equação
print("Intercepto (α):", modelo.intercept_)
print("Coeficiente (β):", modelo.coef_[0])