#exercicio 1
# Initialize offset
offset = 8

# Code the while loop
while offset!= 0:
    print('correcting..')
    offset -= 1
    print(offset)

#exercicio 2
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset -= 1
    else : 
      offset += 1   
    print(offset)

#exercicio 3
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for i in areas:
    print(i)

#exercicio 4
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for i, a in enumerate(areas):
    print(f'room {i}: {a}')

#exercicio 5
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(area))

#exercicio 6
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
# Loop through each sub-list
for room in house:
    name = room[0]   # nome do cômodo
    area = room[1]   # área do cômodo
    print(f'the {name} is {area} sqm')

##############################################
world = {'vitoria': 18,
         'alfredo': 20,
         'henrique': 8}
for key, value in world.items(): 
    print(key + ' -- ' + str(value)) 


import numpy as np

np_height = np.array([1.73, 1.66, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 58.4, 0.71])
bmi = np_weight / np_height ** 2
for val in bmi: #sai um elemento por vez
    print(val)

meas = np.array([np_height, np_weight])
for val in np.nditer(meas): #nditer = n-dimensional iterator (para arrays multidimensionais), para sair um elemento por vez
    print(val)