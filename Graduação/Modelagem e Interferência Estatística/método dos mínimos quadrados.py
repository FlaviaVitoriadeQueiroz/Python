from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.outliers_influence import variance_inflation_factor


# Dados

X = np.array([
    [0, 2],
    [2, 6],
    [2, 7],
    [2, 5],
    [4, 9],
    [4, 8],
    [4, 7],
    [6, 10],
    [6, 11],
    [6, 9],
    [8, 15],
    [8, 13]
])

y = np.array([2, 3, 2, 7, 6, 8, 10, 7, 8, 12, 11, 14])


# Divisão treino/teste

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Modelo

model = LinearRegression()
model.fit(X_train, y_train)

# Coeficientes

print("Intercepto (β0):", model.intercept_)
print("Coeficientes (β1, β2):", model.coef_)


# Previsões

y_pred = model.predict(X_test)


# Avaliação

print("\nR²:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))


# Resíduos

residuos = y_test - y_pred

# Gráfico resíduos vs previsão
plt.scatter(y_pred, residuos)
plt.axhline(0)
plt.xlabel("Valores previstos")
plt.ylabel("Resíduos")
plt.title("Resíduos vs Previsões")
plt.show()


# Normalidade dos resíduos

stats.probplot(residuos, dist="norm", plot=plt)
plt.title("QQ Plot dos Resíduos")
plt.show()


# Independência (Durbin-Watson)

print("\nDurbin-Watson:", durbin_watson(residuos))


# Multicolinearidade (VIF)

vif = [variance_inflation_factor(X, i) for i in range(X.shape[1])]
print("VIF:", vif)


'''O que esse código agora faz

✔️ Treina corretamente
✔️ Testa em dados novos (mais confiável)
✔️ Mostra qualidade do modelo
✔️ Analisa resíduos visualmente
✔️ Testa normalidade
✔️ Verifica independência
✔️ Detecta multicolinearidade'''


'''Você faz tudo isso para:

garantir confiabilidade
evitar erro de interpretação
tomar decisões melhores
transformar dados em valor real'''