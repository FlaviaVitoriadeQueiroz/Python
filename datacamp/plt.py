import matplotlib.pyplot as plt 

years = [1890, 1590, 1870, 1900, 2000, 1290, 2010]
pop = [7.2, 7.8, 6.5, 3.8, 9.8, 3.7, 12.8] #dados ficticios

plt.plot(years, pop) #primeiro eixo horizontal, segundo eixo vertical
plt.show()


ano = [1950, 2010, 2022, 2024]
populacao = [2.5, 6.8, 8, 8.2] #dados da ONU

plt.plot(ano, populacao) #grafico de linha
plt.show()

ano = [1950, 2010, 2022, 2024]
populacao = [2.5, 6.8, 8, 8.2] #dados da ONU

plt.scatter(ano, populacao) #grafico de pontos
plt.show()