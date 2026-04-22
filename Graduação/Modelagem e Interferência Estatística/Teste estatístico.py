import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import scipy.stats as stats


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

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Modelo

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
residuos = y_test - y_pred


# Avaliação básica

print("R²:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))


# 🔬 Teste de Shapiro-Wilk (Normalidade)

shapiro_stat, shapiro_p = stats.shapiro(residuos)

print("\nTeste de Shapiro-Wilk:")
print("Estatística:", shapiro_stat)
print("p-valor:", shapiro_p)

if shapiro_p > 0.05:
    print("→ Resíduos parecem normais (OK)")
else:
    print("→ Resíduos NÃO são normais (Problema)")


# Teste de Bartlett (Homocedasticidade)

# Dividindo resíduos em 2 grupos (exemplo simples)
grupo1 = residuos[:len(residuos)//2]
grupo2 = residuos[len(residuos)//2:]

bartlett_stat, bartlett_p = stats.bartlett(grupo1, grupo2)

print("\nTeste de Bartlett:")
print("Estatística:", bartlett_stat)
print("p-valor:", bartlett_p)

if bartlett_p > 0.05:
    print("→ Variâncias são iguais (OK - homocedasticidade)")
else:
    print("→ Variâncias diferentes (Problema)")