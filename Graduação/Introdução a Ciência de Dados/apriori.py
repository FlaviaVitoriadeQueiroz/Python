''' Criei uma versão minha do código disponível para a realização da atividade da unidade 3 de Mineração de Dados.
Preferi criar um c[odigo proprio para praticar realmente o que foi visto em aula e no codigo fornecido.'''


import pandas as pd
from mlxtend.frequent_patterns import apriori #é uma boa prática importar as bibliotecas no início do código, para facilitar a leitura e organização do código. Modificação 1

''' mlxtend é uma biblioteca que fornece implementações eficientes de algoritmos de mineração de dados,
incluindo o algoritmo Apriori . O Apriori é um algoritmo clássico usado para regras de associação, que identifica padrões frequentes em grandes conjuntos de dados transacionais.
Ele funciona iterativamente, gerando candidatos a conjuntos frequentes e filtrando-os com base em um suporte mínimo definido pelo usuário.
O mlxtend facilita a aplicação do Apriori em conjuntos de dados, permitindo que os usuários encontrem rapidamente padrões e associações significativas entre'''

# Create false dataset

columns = ['ID', 'beer', 'gum', 'butter', 'eggs', 'diapers', 'milk', 'bread', 'coke', 'snacks'] # Modificação 2: Acrescentei mais produtos 
dataset = [[1, 1, 0, 0, 1, 1, 0, 0, 1, 0],
           [2, 0, 1, 0, 0, 1, 1, 0, 0, 1],
           [3, 1, 0, 1, 0, 0, 1, 0, 1, 0],
           [4, 0, 1, 0, 1, 0, 0, 1, 0, 1],
           [5, 1, 0, 0, 1, 1, 0, 0, 1, 0],
           [6, 0, 1, 0, 0, 1, 1, 0, 0, 1],
           [7, 1, 0, 1, 0, 0, 1, 0, 1, 0],
           [8, 0, 1, 0, 1, 0, 0, 1, 0, 1],
           [9, 1, 0, 0, 1, 1, 0, 0, 1, 0],
           [10, 0, 1, 0, 0, 1, 1, 0, 0, 1],
           [11, 1, 0, 1, 0, 0, 1, 0, 1, 0],
           [12, 0, 1, 0, 1, 0, 0, 1, 0, 1],
           [13, 1, 0, 0, 1, 1, 0, 0, 1, 0],
           [14, 0, 1, 0, 0, 1, 1, 0, 0, 1],
           [15, 1, 0, 1, 0, 0, 1, 0, 1, 0],
           [16, 0, 1, 0, 1, 0, 0, 1, 0, 1],
           [17, 1, 0, 0, 1, 1, 0, 0, 1, 0],
           [18 ,0 ,1 ,0 ,0 ,1 ,1 ,0 ,0 ,1],
           [19 ,1 ,0 ,1 ,0 ,0 ,1 ,0 ,1 ,0],
           [20 ,0 ,1 ,0 ,1 ,0 ,0 ,1 ,0 ,1]]
# estou usando uma dataset relativamente maior em comparação com o exemplo. Modificação 3

df = pd.DataFrame(dataset, columns=columns) 

# print(df)



# Apriori
'''Essa classe é responsável por executar o algoritmo Apriori no DataFrame fornecido,
permitindo a identificação de padrões frequentes e regras de associação com base em um suporte mínimo definido pelo usuário.'''

'''O método __init__ é o construtor da classe Apriori, responsável por inicializar a instância com um DataFrame,
um valor opcional de suporte mínimo e uma opção para transformar os dados em booleanos. 
Ele valida o DataFrame, armazena-o na instância e, se necessário, transforma os dados em booleanos para uso no algoritmo Apriori.'''

class Apriori:
    threshold = 0.5 # Valor padrão para o suporte mínimo
    df = None # Cria um DF vazio para ser preenchido posteriormente

    def __init__(self, df, threshold=None, transform_bol=False): 
        
        self._validate_df(df) # Valida o DataFrame fornecido, garantindo que seja um objeto pandas.DataFrame válido. Se o DataFrame for inválido, uma exceção é levantada.

        self.df = df # Armazena o DataFrame na instância da classe para uso posterior em outros métodos.
        if threshold is not None: # Se um valor de suporte mínimo for fornecido, ele é armazenado na instância da classe para ser usado no algoritmo Apriori. Caso contrário, o valor padrão de 0.5 será utilizado.
            self.threshold = threshold 

        if transform_bol: 
            self._transform_bol() # Se a opção transform_bol for verdadeira, os dados do DataFrame são transformados em booleanos (True/False) usando o método _transform_bol, preparando-os para a aplicação do algoritmo Apriori.

    def _validate_df(self, df=None): 
        

        if df is None:
            raise Exception("df must be a valid pandas.DataDrame.") # Verifica se o DataFrame é None e, se for, levanta uma exceção indicando que um DataFrame válido deve ser fornecido.


    def _transform_bol(self):
        
        for column in self.df.columns:
            self.df[column] = self.df[column].apply(lambda x: True if x == 1 else False) # Transforma os dados do DataFrame em booleanos, onde os valores iguais a 1 são convertidos para True e os valores diferentes de 1 são convertidos para False. Isso é feito iterando sobre cada coluna do DataFrame e aplicando a transformação usando a função apply.


    def _apriori(self, use_colnames=False, max_len=None, count=True):
        
        apriori_df = apriori(
                    self.df, 
                    min_support=self.threshold,
                    use_colnames=use_colnames, 
                    max_len=max_len
                )
        if count:
            apriori_df['length'] = apriori_df['itemsets'].apply(lambda x: len(x))

        return apriori_df

    def run(self, use_colnames=False, max_len=None, count=True):
        

        return self._apriori(
                        use_colnames=use_colnames,
                        max_len=max_len,
                        count=count
                    )

    def filter(self, apriori_df, length, threshold):
        
        
        if 'length' not in apriori_df.columns:
            raise Exception("apriori_df has no length. Please run the Apriori with count=True.")

        return apriori_df[ (apriori_df['length'] == length) & (apriori_df['support'] >= threshold) ]
    

if 'ID' in df.columns: del df['ID'] # Remove a coluna 'ID' do DataFrame, se ela existir, para garantir que apenas os dados relevantes sejam usados na aplicação do algoritmo Apriori.

apriori_runner = Apriori(df, threshold=0.3, transform_bol=True) # Cria uma instância da classe Apriori, passando o DataFrame df, definindo um suporte mínimo de 0.4 e indicando que os dados devem ser transformados em booleanos para uso no algoritmo Apriori.
apriori_df = apriori_runner.run(use_colnames=True) # Executa o método run da instância apriori_runner, que aplica o algoritmo Apriori ao DataFrame, retornando um DataFrame com os padrões frequentes encontrados, usando os nomes das colunas originais em vez de índices numéricos.

print(apriori_df) # Coloquei print pois estou usando o vscode e não o colab

# No final não achei muitas coisas que pudessem ser modificadas, pois o código já estava bem estruturado e organizado

# support = frequência de um item ou conjunto de itens em relação ao total de transações. 
# itemsets = itens ou conjuntos de itens que aparecem juntos em uma transação.
# length = número de itens em um itemset.

'''Conclusão:
Gum e snacks devem ficar próximos, pois aparecem juntos em muitas transações.
Coke e beer também devem ficar próximos, pois aparecem juntos em muitas transações.'''
