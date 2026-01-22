import matplotlib.pyplot as plt

lista_numerica = [2, 4, 0, 0, 5, 6, 8, 9, 7, 0.99]
plt.hist(lista_numerica, bins=6) 
plt.show()

ano = [2007, 2014, 2030, 2050, 2100, 2130]
populacao = [6.7, 7.3, 9.12, 10.4, 10.2, 14]
plt.plot(ano, populacao)
plt.show()

plt.scatter(ano, populacao)
plt.show()