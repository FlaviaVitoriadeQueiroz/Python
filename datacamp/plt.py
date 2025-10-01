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

#exercicio 1
print(years)
print(pop)

import matplotlib.pyplot as plt

plt.plot(years, pop)
plt.show()

#exercicio 2
'''print(gdp_cap[-1])
print(life_exp[-1])

import matplotlib.pyplot as plt 
plt.plot(gdp_cap, life_exp)
plt.show()'''

#exercicio 3
'''plt.scatter(gdp_cap, life_exp) #gráfico de dispersão
plt.xscale('log') #muda o eixo X para logarítmico
plt.show()'''

#exercicio 4