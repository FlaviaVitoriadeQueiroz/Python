import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sweetviz as sv # Biblioteca para análise exploratória de dados

minutopordia = np.random.randint(0, 60, 30)
print(minutopordia)



# Gráfico 
ax=sns.histplot(minutopordia)
ax.set(xlabel="Minutos por dia", ylabel="Frequência")
ax.set_title("Distribuição de Minutos por Dia")
plt.show()



# Análise Exploratória de Dados com Sweetviz

arquivo = 'https://raw.githubusercontent.com/JeffSackmann/tennis_atp/master/atp_matches_2021.csv'
dados = pd.read_csv(arquivo)
#print(dados)

dados_numericos = dados.select_dtypes(include=[np.number])

eda=sv.analyze(dados)
eda.show_html('relatorio_sweetviz.html') # Gera um relatório HTML interativo com a análise exploratória dos dados
#file:///B:/Github/Python/Ci%C3%AAncia%20de%20Dados/relatorio_sweetviz.html



# Gerar uma matriz de correlação (de Pearson) de variáveis numéricas
mask = np.triu(np.ones_like(dados_numericos.corr(), dtype=bool)) # Cria uma máscara para ocultar a parte superior da matriz de correlação

corr = dados_numericos.corr()

n = len(dados_numericos.columns)
plt.figure(figsize=(n * 0.8, n * 0.8)) # Define o tamanho da figura

sns.heatmap(
    dados_numericos.corr(),
    mask=mask,
    square = True,
    annot=True,
     fmt=".2f",
    annot_kws={"size": 8},
    vmin=-1,
    vmax=1, # Plota a matriz de correlação usando um mapa de calor
    cmap="coolwarm")

plt.xticks(rotation=45, ha='right', fontsize=8)
plt.yticks(fontsize=8)

plt.tight_layout()
plt.show()

'''A matriz de Pearson é uma medida de correlação linear entre variáveis numéricas, variando de -1 a 1.
Valores próximos a 1 indicam uma forte correlação positiva, o mais escuro
valores próximos a -1 indicam uma forte correlação negativa, quando uma variável aumenta, a outra tende a diminuir, o mais clarinho
e valores próximos a 0 indicam pouca ou nenhuma correlação linear entre as variáveis.'''