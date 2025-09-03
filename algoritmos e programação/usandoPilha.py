#implementacao de uma pilha sequencial
class Pilha:
    def __init__(self, tamanho): #construtor
        self.tamanho = tamanho #tamanho maximo da pilha
        self.dados = [None] * tamanho #array fixo, com um tanto X (de acordo com o tamanho da pilha)de elementos vazios
        self.topo = -1 #indice do topo da pilha

    def push(self, elemento):
        if self.topo < self.tamanho -1: #menos -1 pq comeca no 0
            self.topo +=1 #incrementa o indice do topo 
            self.dados[self.topo] = elemento #coloca o elemento no local que o indice esta marcando (o topo)
            print(f"Elemento {elemento} inserido.")
        else:
            print("Erro: Pilha cheia.")

    def pop(self):
        if self.topo >= 0: #pq se o indicador esta em -1, a pilha esta vazia, e n tem oq ser retirado
            elemento = self.dados[self.topo] #seleciona o elemento do topo
            self.dados[self.topo] = None #remove o elemento do topo
            self.topo -= 1 #desce o marcador
            print(f"Elemento {elemento} removido.")
            return elemento
        else:
            print("Erro: Pilha vazia.")
            return None

    def top(self):
        if self.topo >= 0: #pq se o indicador esta em -1, a pilha esta vazia, e n tem oq ser retirado
            return self.dados[self.topo] #retorna o elemento que estiver no topo
        else:
            print("Erro: Pilha vazia.")
            return None

#Nao e uma operacao basica da estrutura de dados, mas e recomendado ter em todas as estruturas
    def imprimir(self):
        print("Elementos da Pilha:", self.dados) #com self.dados da para imprimir tudo que estiver na estrutura com uma linha de codigo so, mas tambem pode fazer com lacos

#Usando
pilha = Pilha(9)
pilha.push(9)
pilha.push(12)
pilha.push(18)
pilha.push(21)
pilha.imprimir()
print("Elemento no topo:", pilha.top())
pilha.pop()
pilha.pop()
pilha.imprimir()
pilha.push(8)
pilha.push(11)
pilha.push(15)
pilha.push(22)
pilha.push(10)
pilha.push(24)
pilha.push(28)
pilha.push(31)