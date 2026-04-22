# Para Exploração de dados
import pandas as pd
import matplotlib.pyplot as plt

# Exemplo de dados
dados = {
    "horas_estudo": [2, 3, 5, 6, 8],
    "nota": [5, 6, 7, 8, 9]
}

df = pd.DataFrame(dados)

# Correlação de Pearson
correlacao = df["horas_estudo"].corr(df["nota"])

# Interpretanto a saída
if correlacao > 0.7:
    print('Correlação forte positiva')
elif correlacao > 0.3:
    print('Correlação moderada positiva')
elif correlacao > 0:
    print('Correlação fraca positiva')
elif correlacao < -0.7:
    print('Correlação forte negativa')
elif correlacao < -0.3:
    print('Correlação moderada negativa')
elif correlacao < 0:
    print('Correlação fraca negativa')
else:
    print('Sem correlação linear')


# Criando um gráfico de linha
plt.plot(df['horas_estudo'], df['nota'], marker='o')
plt.xlabel('Horas de estudo')
plt.ylabel('Nota na prova')
plt.title('Relação entre horas de estudo e nota')
plt.grid(True)
plt.show()

# Para Validação estatística
from scipy.stats import pearsonr

x = [2, 3, 5, 6, 8]
y = [5, 6, 7, 8, 9]

r, p_valor = pearsonr(x, y)

# Interpretanto a saída
if correlacao > 0.7:
    print('Correlação forte positiva')
elif correlacao > 0.3:
    print('Correlação moderada positiva')
elif correlacao > 0:
    print('Correlação fraca positiva')
elif correlacao < -0.7:
    print('Correlação forte negativa')
elif correlacao < -0.3:
    print('Correlação moderada negativa')
elif correlacao < 0:
    print('Correlação fraca negativa')
else:
    print('Sem correlação linear')

# Interpretação do p-valor
if p_valor < 0.05:
    print("Resultado estatisticamente significativo (evidência de relação real)")
else:
    print("Resultado NÃO significativo (pode ser ao acaso)")

'''O p-valor é uma medida usada na estatística para ajudar a decidir se um resultado é real ou apenas fruto do acaso.
p-valor pequeno (geralmente < 0,05) → evidência contra o acaso → resultado estatisticamente significativo
p-valor grande (≥ 0,05) → pode ter acontecido por acaso → não é possível afirmar efeito real'''