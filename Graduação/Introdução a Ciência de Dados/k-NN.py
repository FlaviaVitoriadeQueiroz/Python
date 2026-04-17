import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler


# Load the dataset
df = sns.load_dataset('iris')

# EDA
print("--- PRIMEIRAS LINHAS DO DATASET ---")
print(df.head())

# Vendo quantas flores de cada tipo temos
print("\n--- CONTAGEM DE CADA CLASSE ---")
print(df['species'].value_counts())

# Visualização
sns.scatterplot (data=df, x='petal_length', y='petal_width', hue='species') #hue para colorir os pontos de acordo com a espécie 
plt.title('Distribuição das Flores por Comprimento e Largura da Pétala')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()


