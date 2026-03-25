#exercicio 1
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for x, y in europe.items():
    print(f"the capital of {x} is {y}")

#exercicio 2
# Import numpy as np
'''import numpy as np

# For loop over np_height
for x in np_height:
    print(f'{x} inches')

# For loop over np_baseball
for i in np.nditer(np_baseball):
    print(i)'''

#loops em pandas
import pandas as pd
brics1 = pd.read_csv("B:/VScode/Python/cursos/brics.csv", index_col=0) #index_col=0 para usar a primeira coluna como indice, em vez de criar um novo indice numerico
print(brics1)

for lab, row in brics1.iterrows():
    print(lab)
    print(row)

#para imprimir apenas a capital:
for lab, row in brics1.iterrows():
    print(lab + ':' + row[' capital'])

#adicionando uma nova coluna
for lab, row in brics1.iterrows():
    brics1.loc[lab, 'name_length'] = len(row['country'])
print(brics1)

#outra maneira muito mais eficiente de se fazer isso:
brics1['name_length'] = brics1['country'].apply(len) #aplica a funcao len a cada elemento da coluna country
#e mais eficiente pq nao precisa iterar linha por linha e atribuir o valor
print(brics1)

#exercicio 3
# Import cars data
'''import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for i, j in cars.iterrows():
    print(i)
    print(j)'''

#exercicio 4
# Import cars data
'''import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows():
    print(lab + ': ' + str(row['cars_per_cap'])) #str() converte numero em texto'''

#exercicio 5
# Import cars data
'''import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, 'COUNTRY'] = row['country'].upper()


# Print cars
print(cars)'''

#exercicio 6
'''# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars['country'].apply(str.upper)'''