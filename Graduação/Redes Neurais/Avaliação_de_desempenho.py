from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Dados fictícios de exemplo
'''preto = 1
vermelho = 2
azul = 3'''

y_real = [1, 2, 1, 3, 2, 1, 3, 2, 1, 3]  # Valores reais das classes
y_pred = [1, 2, 1, 3, 2, 1, 3, 2, 1, 3]  # Valores previstos pelo modelo


# Calcula a matriz de confusão
cm = confusion_matrix(y_real, y_pred)

print("Matriz de Confusão:")
print(cm)
print("\nRelatório de Classificação:")
print(classification_report(y_real, y_pred))  # Exibe o relatório de classificação


# Gráfico da matriz de confusão

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues') # cm é a matriz de confusão, annot=True adiciona os valores na célula, fmt='d' formata os valores como inteiros, cmap define o mapa de cores
plt.title('Matriz de Confusão')
plt.xlabel('Valores Previstos')
plt.ylabel('Valores Reais')
plt.show()

# Métricas de desempenho adicionais
accuracy = np.trace(cm) / np.sum(cm)  # Acurácia: proporção de previsões corretas em relação ao total de previsões
precision = np.diag(cm) / np.sum(cm, axis=0)  # Precisão: proporção de verdadeiros positivos em relação ao total de positivos previstos
recall = np.diag(cm) / np.sum(cm, axis=1)  #    Sensibilidade (Recall): proporção de verdadeiros positivos em relação ao total de positivos reais   
f1_score = 2 * (precision * recall) / (precision + recall)  # F1 Score: média harmônica entre precisão e sensibilidade
support = np.sum(cm, axis=1)  # Suporte: número de ocorrências reais de cada classe
macro_precision = np.mean(precision)  # Precisão macro: média das precisões de todas as classes
macro_recall = np.mean(recall)  # Sensibilidade macro: média das sensibilidades
macro_f1_score = np.mean(f1_score)  # F1 Score macro: média dos F1 Scores de todas as classes
weighted_precision = np.sum(precision * support) / np.sum(support)  # Precisão ponderada: média ponderada das precisões, considerando o suporte de cada classe
weighted_recall = np.sum(recall * support) / np.sum(support)  # Sensibilidade ponderada: média ponderada das sensibilidades, considerando o suporte de cada classe
weighted_f1_score = np.sum(f1_score * support) / np.sum(support)  # F1 Score ponderado: média ponderada dos F1 Scores, considerando o suporte de cada classe