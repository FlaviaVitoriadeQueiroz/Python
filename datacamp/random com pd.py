# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)
# Generate and print random float
print(np.random.rand())

#exercicio 1
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))

#exercicio 2
# NumPy is imported, seed is set
import numpy as np
# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1, 7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice == 3 or dice == 4 or dice == 5:
    step += 1
else:
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice, step)

###################
np.random.seed(123)
outcomes = []
for x in range(10):
    coin = np.random.randint(0,2) #0 ou 1
    if coin == 0:
        outcomes.append('heads')
    else:
        outcomes.append('tails')
print(outcomes)

#para que fique mais aleatorio:
np.random.seed(123)
tails = [0]
for x in range(10):
    coin = np.random.randint(0,2) #0 ou 1
    tails.append(tails[x] + coin)
print(tails)