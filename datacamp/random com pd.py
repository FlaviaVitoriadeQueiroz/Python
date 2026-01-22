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


#exercicio 3
# NumPy is imported, seed is set
import numpy as np
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

for x in range(100):
    step = random_walk[-1]
    dice = np.random.randint(1, 7)

    if dice <= 2:
        # step não pode ficar abaixo de 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)

    random_walk.append(step)

print(random_walk)


#exercicio 4
# NumPy is imported, seed is set
import numpy as np
np.random.seed(123)

# Initialize random_walk
random_walk = [0]  # começa em 0

# Complete the loop: iterate 100 times (por exemplo)
for x in range(100):
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1, 7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)


#exercicio 5
# NumPy is imported, seed is set
import numpy as np
np.random.seed(123)

# Initialization
random_walk = [0]

for x in range(100):
    step = random_walk[-1]
    dice = np.random.randint(1, 7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)
plt.title("Random Walk Simulation")
plt.xlabel("Step")
plt.ylabel("Position")

# Show the plot
plt.show()


#exercicio 6
# NumPy is imported; seed is set
import numpy as np
np.random.seed(123)

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk five times
for i in range(5):  # iterar 5 vezes

    # Code from before
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)


#exercicio 7
# numpy and matplotlib imported, seed set
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)

# initialize and populate all_walks
all_walks = []
for i in range(5):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.title("Random Walks (5 simulations)")
plt.xlabel("Step")
plt.ylabel("Position")
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np_aw.T

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.title("Random Walks Transposed")
plt.xlabel("Step")
plt.ylabel("Position")
plt.show()


#exercicio 8
# numpy and matplotlib imported, seed set
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)

# clear the plot
plt.clf()

# Initialize all_walks
all_walks = []

# Simulate random walk 20 times
for i in range(20):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)

        # Implement clumsiness: 0.5% chance to reset to 0
        if np.random.rand() <= 0.005:
            step = 0

        random_walk.append(step)
    
    # Append the random_walk to all_walks
    all_walks.append(random_walk)

# Convert to NumPy array and plot (optional)
np_aw_t = np.array(all_walks).T
plt.plot(np_aw_t)
plt.show()


#exercicio 9
# numpy and matplotlib imported, seed set
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)

# Simulate random walk 500 times
all_walks = []
for i in range(500):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001:
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1, :]  # última linha, todas as colunas

# Plot histogram of ends, display plot
plt.hist(ends)
plt.title("Histogram of Random Walk Ends (500 simulations)")
plt.xlabel("Position at Step 100")
plt.ylabel("Frequency")
plt.show()
