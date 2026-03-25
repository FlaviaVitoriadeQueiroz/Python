""" As filas seguem o principio FIFO
Suas operacoes basicas sao:
inserir/enfileirar, so coloca no final
remover/desenfileirar, so remove no inicio
buscar/primeiro, so pode ocorrer no inicio

o marcador final sempre marcara a proxima posicao livre, que sera ocupada em seguida"""

#Implementacao de Fila
class Fila:
    def __init__(self, tamanho): #construtor
        self.tamanho = tamanho #tamanho maximo da fila
        self.dados = [None] * tamanho #array fixo, com um tanto X (de acordo com o tamanho da fila) de elementos vazios
        self.inicio = 0 #indice do inicio da fila, onde ocorre a remocao
        self.fim = 0 #indice do fim da fila, onde ocorre a insercao
        self.quantidade = 0 #quantidade atual de elementos na fila

    def enfileirar(self, elemento):
        if self.quantidade < self.tamanho: #verifica se a fila n esta cheia
            self.dados[self.fim] = elemento #insere o elemento no fim da fila
            self.fim += 1 #atualiza o indice para o fim da fila
            self.quantidade += 1 #atualiza a quantidade de elementos na fila
            print(f"Elemento {elemento} enfileirado.")
        else:
            print("Erro: Fila cheia.")

    def desenfileirar(self):
        if self.quantidade > 0: #verifica se a fila n esta vazia, pq n da para tirar oq nao ha
            elemento = self.dados[self.inicio] #armazena o elemento a ser removido do inicio
            self.dados[self.inicio] = None #remove o elemento do inicio da fila
            self.inicio += 1 #atualiza o indice para o inicio da fila
            self.quantidade -= 1 #atualiza a quantidade de elementos na fila
            print(f"Elemento {elemento} desenfileirado.")
            return elemento
        else:
            print("Erro: Fila vazia.")
            return None
        
        def primeiro(self):
            if self.quantidade > 0:
                return self.dados[self.inicio]
            else:
                print("Erro: Fila vazia.")
                return None

        '''def imprimir(self):
            if self.quantidade > 0:
                print("Fila:", end=" ")
                for i in range(self.quantidade):
                    print(self.dados[(self.inicio + i) % self.tamanho], end=" ")
                print()
            else:
                print("Erro: Fila vazia.")'''

                #ou

        def imprimir(self):
            print("Elementos da Fila:", self.dados)
