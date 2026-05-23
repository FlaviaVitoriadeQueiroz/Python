import pandas as pd

dados = {
    "Nome": ["Ana", "Carlos"],
    "Idade": [20, 30],
    "Salario": [2500.50, 4000.00]
}

df = pd.DataFrame(dados)

# A função dtypes é usada para verificar os tipos de dados de cada coluna em um DataFrame.
print(df.dtypes)

# A função columns retorna os nomes das colunas do DataFrame.
print(df.columns)

# A função tolist() é usada para converter um objeto em uma lista. No caso de df.columns, ela converte os nomes das colunas em uma lista usando o método tolist().
print(df.columns.tolist())

# A função select_dtypes() é usada para selecionar colunas de um DataFrame com base em seus tipos de dados. 
# O parâmetro include='object' seleciona apenas as colunas que contêm dados do tipo objeto (geralmente strings).
colunas_texto = df.select_dtypes(include='object').columns.tolist()
print(colunas_texto)





dados1= {
    "Nome": ["Ana", "Carlos", "Maria", "João", "Pedro", "Julia"],
    "Idade": [20, 17, 25, 30, 16, 22]
}

df = pd.DataFrame(dados1)

# Query para selecionar apenas as linhas onde a idade é maior que 18
maiores_de_idade = df.query("Idade > 18")
print(maiores_de_idade)

# .sample é um método do pandas que permite selecionar uma amostra aleatória de linhas de um DataFrame.
amostra_aleatoria = df.sample(n=3)  # Seleciona 3 linhas aleatórias
print(amostra_aleatoria)




'''o .agg() (abreviação de aggregate) serve para aplicar uma ou várias funções de resumo estatístico em colunas de um DataFrame ou Series.'''
import pandas as pd

# Simulando dados de notas
df = pd.DataFrame({
    "NU_NOTA_MT": [450, 600, 750, 800, 500],
    "NU_NOTA_CN": [500, 650, 700, 820, 480]
})

# Usando agg para várias estatísticas ao mesmo tempo
resultado = df.agg({
    "NU_NOTA_MT": ["mean", "min", "max", "std"],
    "NU_NOTA_CN": ["mean", "min", "max", "std"]
})

print(resultado)


# Só sera retornado as linhas onde a nota de matemática é maior que 500 e a nota de ciências é maior que 600.
df.query('NU_NOTA_MT > 500 and NU_NOTA_CN > 600')
print(df.query('NU_NOTA_MT > 500 and NU_NOTA_CN > 600'))

# Só retorna as linhas onde a nota de matemática é maior que 500 ou a nota de ciências é maior que 600.
df.query('NU_NOTA_MT > 500 or NU_NOTA_CN > 600')
print(df.query('NU_NOTA_MT > 500 or NU_NOTA_CN > 600'))



# Criando outra lista que contenha o sexo dos alunos
df["TP_SEXO"] = ["F", "M", "F", "M", "M"]

# Criando uma máscara boolean 
df.TP_SEXO == "F"
# Usando a máscara para filtrar o DataFrame e retornar apenas as linhas onde o sexo é feminino
df.query('TP_SEXO == "F"')  
print(df.query('TP_SEXO == "F"'))



# Condições
condição1 = df["NU_NOTA_MT"] > 500
condição2 = df["NU_NOTA_CN"] > 600
df.loc[condição1 & condição2]  # Usando loc para filtrar o DataFrame com as condições combinadas usando o operador & (AND)
print(df.loc[condição1 & condição2])



# Criando outra lista que tenha cidade

df = pd.DataFrame({
    "Nome": ["Ana", "Carlos", "Maria", "João"],
    "Cidade": ["SP", "RJ", "MG", "SP"]
})

# Usando isin para filtrar o DataFrame e retornar apenas as linhas onde a cidade é SP ou RJ
df.query('Cidade.isin(["SP", "RJ"])')
print(df.query('Cidade.isin(["SP", "RJ"])'))

# Usando - para negar a condição e retornar as linhas onde a cidade não é SP ou RJ
df.query('not Cidade.isin(["SP", "RJ"])')   
print(df.query('not Cidade.isin(["SP", "RJ"])'))



# contains é um método usado para verificar se uma string contém uma substring específica. Ele retorna True se a substring for encontrada e False caso contrário.
# Usando contains para filtrar o DataFrame e retornar apenas as linhas onde a cidade contém a letra "S"
# atr. é usado para acessar os atributos de uma coluna em um DataFrame. Ele é útil para acessar métodos e propriedades específicas de uma coluna, como str para operações de string ou dt para operações de data.
df.query('Cidade.str.contains("S")')    
print(df.query('Cidade.str.contains("S")'))




# Ordenando o DataFrame por idade em ordem crescente, usando o método sort_values() do pandas.
#  O parâmetro by especifica a coluna pela qual queremos ordenar, e o parâmetro ascending=True indica que queremos uma ordenação crescente.
df.sort_values(by="Idade", ascending=True)

# Podemos definir onde queremos colocar os valores ausentes usando o parâmetro na_position. Por exemplo, se quisermos colocar os valores ausentes no início da ordenação, podemos usar na_position='first'.
df.sort_values(by="Idade", ascending=True, na_position='first')

# Ordenando o DataFrame por mais de uma coluna 
df.sort_values(by=["Idade", "Nome"], ascending=[True, False]) 
# Ordena primeiro por idade em ordem crescente e, em caso de empate na idade, ordena por nome em ordem decrescente.


# Função nlargest() é usada para retornar as n maiores linhas de um DataFrame com base em uma coluna específica.
# Por exemplo, para obter as 3 maiores idades do DataFrame, podemos usar:   
df.nlargest(3, "Idade")

# Enquando a função nsmallest() é usada para retornar as n menores linhas de um DataFrame com base em uma coluna específica.
# Por exemplo, para obter as 3 menores idades do DataFrame, podemos usar:
df.nsmallest(3, "Idade")

# Essas funções co keepm são úteis para obter rapidamente os valores mais altos ou mais baixos em uma coluna, sem precisar ordenar todo o DataFrame. 
# Elas são otimizadas para desempenho e podem ser mais eficientes do que usar sort_values() seguido de head() ou tail() para obter os mesmos resultados.
df.nlargest(3, "Idade", keep="all")  # Retorna as 3 maiores idades, incluindo empates
df.nsmallest(3, "Idade", keep="all")  # Retorna as 3 menores idades, incluindo empates  
#keep pode ser 'first' (padrão), 'last' ou 'all', indicando como lidar com empates.
#  'first' mantém apenas a primeira ocorrência, 'last' mantém a última ocorrência e 'all' mantém todas as ocorrências empatadas.




# Mudando o index do DataFrame para a coluna "Nome" usando o método set_index() do pandas.
df.set_index("Nome", inplace=True)  # inplace=True para modificar o DataFrame original

# Ordenando o DataFrame pelo índice (que agora é a coluna "Nome") usando o método sort_index() do pandas.
df.sort_index(inplace=True)  # inplace=True para modificar o DataFrame original



# Multi index ou índex hierárquico é um recurso do pandas que permite criar índices compostos por múltiplos níveis.
#  Ele é útil para organizar dados que possuem uma estrutura hierárquica, como dados de vendas por região e por produto, ou dados de alunos por turma e por disciplina.
# Podemos escolher mais de uma coluna para ser o índice do DataFrame, passando uma lista de colunas para o método set_index().
#  Por exemplo, se quisermos usar as colunas "Nome" e "Cidade" como índice, podemos fazer:
df.set_index(["Nome", "Cidade"], inplace=True)  # Usando as colunas "Nome" e "Cidade" como índice

# Para resetar o índice do DataFrame e voltar a usar um índice numérico padrão, podemos usar o método reset_index() do pandas. Por exemplo:
df.reset_index(inplace=True)  # Resetando o índice para um índice numérico padrão   


