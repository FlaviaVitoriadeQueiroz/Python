import pandas as pd

customers = pd.read_csv('customers.csv')

# Transform

split_email = customers.email.str.split('@', expand=True) # Separar a coluna email em duas colunas usando o caractere '@' como separador

customers = customers.assign(
    username=split_email[0], # Criar a coluna username com a primeira parte do email
    domain=split_email[1] # Criar a coluna domain com a segunda parte do email
)

