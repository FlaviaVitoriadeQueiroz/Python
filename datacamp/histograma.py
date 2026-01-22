import matplotlib.pyplot as plt 
#se não especificar o bins o padrão é 10

valores = [1, 1.1, 1.4, 2.5, 2, 6.6, 3.4, 3, 4, 5, 5.6, 6, 6.8, 20, 30, 10, 0, 5.9, 7.9, 34.7]
plt.hist(valores, bins=5) #grafico de histograma
plt.show()

#exercico 1
life_exp = [29.9, 33.1, 43.8, 45.7, 51.3, 52.4, 53.6, 55.2, 55.9, 57.2, 58.0, 59.5, 60.0, 60.6]
plt.hist(life_exp, bins=5)
plt.show()
plt.clf()  #Ele limpa o conteúdo da figura atual (o gráfico em construção), mas mantém a janela/figura aberta.
           #Isso é útil quando você quer desenhar um novo gráfico do zero, sem que o anterior continue aparecendo.

plt.hist(life_exp, bins=20)
plt.show()
plt.clf()