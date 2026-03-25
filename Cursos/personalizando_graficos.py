import matplotlib.pyplot as plt 

ano = [1950, 2010, 2022, 2024]
populacao = [2.5, 6.8, 8, 8.2]

#adicionando mais datas
ano = [1800, 1850, 1900] + ano
populacao = [1.0, 1.262, 1.650] + populacao

plt.plot(ano, populacao) 
#personalizando
plt.xlabel('Anos')
plt.ylabel('Populacao em Bilhoes')
plt.title('Crescimento da Populacao ao Longo dos Anos')
plt.yticks([0, 2, 4, 6, 8, 10], #define os valores do eixo y
           [0, '2B', '4B', '6B', '8B', '10B']) #define os nomes dos valores do eixo y
'''plt.xticks([1950, 1975, 2000, 2024]) #define os valores do eixo x'''
plt.show()

#exercicio 1
#a lista do exercicio e a desse script sao diferentes
import numpy as np

np_pop = np.array(ano)
np_pop = np_pop *2

plt.scatter(populacao, ano, s = np_pop)

plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

plt.show()

#exercicio 2
'''plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8) 
#O valor de alfa pode ser definido de 0 a 1, sendo que 0 é totalmente transparente e 1 é completamente opaco.

plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

plt.show()'''

#exercicio 3
'''plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

plt.xscale('log')
#dando nome aos eixos e titulo
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

plt.text(1550, 71, 'India') #adiciona texto no grafico, primeiro valor e eixo x, segundo valor eixo y
plt.text(5700, 80, 'China') #adiciona texto no grafico, primeiro valor e eixo x, segundo valor eixo y
plt.grid(True) #adiciona uma grade ao grafico

plt.show()'''