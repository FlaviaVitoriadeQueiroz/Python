# Transformação logarítmica
import numpy as np

X_log = np.log(X)      # log natural
# ou
X_log10 = np.log10(X)  # log base 10

'''não pode ter valores ≤ 0'''


# Transformação da variável Y
y_log = np.log(y)

'''usada quando a variância aumenta com o valor de y'''


# Transformação inversa (1/X)
X_inv = 1 / X

'''usada quando a relação diminui rapidamente'''


# Raiz quadrada
X_sqrt = np.sqrt(X)

'''suaviza crescimento'''


# Transformação Box-Cox (automática)
from scipy.stats import boxcox

y_boxcox, lambda_ = boxcox(y)

print("Lambda:", lambda_)

'''essa é a mais importante
Ele já retorna:
os dados transformados
o melhor λ'''


# Aplicando no modelo
from sklearn.linear_model import LinearRegression

X_log = np.log(X)

model = LinearRegression()
model.fit(X_log, y)

y_pred = model.predict(X_log)


# Comparando antes e depois
import matplotlib.pyplot as plt

plt.scatter(X[:,0], y)
plt.title("Antes")
plt.show()

plt.scatter(np.log(X[:,0]), y)
plt.title("Depois (log)")
plt.show()


'''| Transformação | Quando usar             |
| ------------- | ----------------------- |
| log           | crescimento exponencial |
| 1/X           | relação decrescente     |
| √X            | suavizar crescimento    |
| Box-Cox       | não sabe qual usar      |
'''
