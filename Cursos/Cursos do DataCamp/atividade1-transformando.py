# Get the rental rate column as a string
# Acessando a coluna rental_rate usando notação de ponto
rental_rate_str = film_df.rental_rate.astype("str")
# sintaxe do comando = nome_do_dataframe.nome_da_coluna.astype("tipo_desejado")


# Split up and expand the column
rental_rate_expanded = rental_rate_str.str.split(".", expand=True)
# sintaxe do comando = nome_do_dataframe.nome_da_coluna.str.split(separador, expand=True)


# Assign the columns to film_df
film_df = film_df.assign(
    rental_rate_dollar=rental_rate_expanded[0],
    rental_rate_cents=rental_rate_expanded[1],
)