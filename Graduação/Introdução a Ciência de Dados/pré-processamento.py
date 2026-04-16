import pandas as pd
import numpy as np
import sweetviz as sv # Biblioteca para análise exploratória de dados


arquivo = "C:/Users/F Vitória de Queiroz/Downloads/df_arabica_clean.csv"
dados = pd.read_csv(arquivo)



print(dados.isnull().sum())
# Na coluna ICO number tem 132 valores nulos, na coluna Farm name tem 2, na Lot number tem 1, na mill tem 3, na region tem 2, na producer tem 1, na processing tem 5



eda=sv.analyze(dados)
eda.show_html('relatorio_sweetviz.html') 


