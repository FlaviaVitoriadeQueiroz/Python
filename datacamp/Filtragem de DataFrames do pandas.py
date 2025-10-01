
dict = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasília", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

brics.index = ['BR', 'RU', 'IN', 'CH', 'SA']

print(brics)
print(brics['area'])
print(brics['area'] > 8)

is_huge = brics['area'] > 8
print(brics[is_huge]) #filtragem, retorna apenas as linhas que satisfazem a condicao

#ou em vez de usar essas duas linhas de codigo podemos usar somente uma
brics[brics['area'] > 8]

import numpy as np
print(np.logical_and(brics['area'] > 8, brics['area'] < 10)) #retorna uma serie de booleanos
print(brics[np.logical_and(brics['area'] > 8, brics['area'] < 10)]) #retorna o dataframe filtrado

#exercicio 1
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)

#exercicio 2
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Subset cars in one line
sel = cars[cars['drives_right']]

# Print sel
print(sel)

#exercicio 3
import pandas as pd

cars = pd.read_csv('cars.csv', index_col=0)

# Create car_maniac: observations that have a cars_per_cap over 500
car_maniac = cars[cars['cars_per_cap'] > 500]

# Print car_maniac
print(car_maniac)


#exercicio 4
import pandas as pd
import numpy as np

# Import cars data
cars = pd.read_csv('cars.csv', index_col=0)

# Create medium: observations with cars_per_cap between 100 and 500
medium = cars[(cars['cars_per_cap'] > 100) & (cars['cars_per_cap'] < 500)]

# Print medium
print(medium)
