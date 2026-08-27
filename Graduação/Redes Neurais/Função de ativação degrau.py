import numpy as np

# Conceito de função de ativação degrau
k = np.array ([-3, -1, 0, 1, 2, 3,])
print(np.where(k>=0)) # printa os indices dos elementos maiores ou iguais a zero
print(np.where(k<0, 's', 'n')) # print a 's' para os elementos menores que zero e 'n' para os elementos maiores ou iguais a zero

'''Em prática a função de ativação degrau é usada para determinar se um neurônio deve ser ativado ou não, com base em um limiar. 
Se a entrada for maior ou igual a zero, o neurônio é ativado (1), caso contrário, ele não é ativado (0).'''

# Função de ativação degrau
x = np.array([[1,2,3], [4,5,6], [7,8,9]])
w = np.array([[1,-3.7,1], [2,2,-2.5]])

print('X: ', x.shape, 'W: ', w.shape)
print('X:\n', x)
print('W:\n', w.T)

z = x @ w.T  # Multiplicação de matrizes usando o operador @ (ou np.dot(x, w.T))
print('Z:\n', z)

def degrauFA(z):
    return np.where(z >= 0, 1, 0) # maior que ou igual a zero retorna 1, caso contrário retorna 0

print('Saída da função de ativação degrau:\n', degrauFA(z))

# Juntando TUDO
h= degrauFA(x @ w.T) # é a primeira camada de uma rede neural, onde a entrada x é multiplicada pelos pesos w e, em seguida, a função de ativação degrau é aplicada ao resultado z para determinar a saída h do neurônio.
print('Saída da função de ativação degrau (h):\n', h)

'''para a segunda camada ficaria h2 = degrauFA(h @ w2.T)
onde w2 são os pesos da segunda camada. A saída h da primeira camada se torna a entrada para a segunda camada, e o processo se repete.'''