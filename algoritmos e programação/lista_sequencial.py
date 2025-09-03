class ListaSquencial:
    def __init__ (self, capacidade): #construtor 
        self.capacidade = capacidade #a capacidade e fixa por ser uma lista sequencial 
        self.dados = [None] * capacidade #array fixo, que vai criar um numero x espacos vazios na memoria de acordo com o valor dado em capacidade
        self.tamanho = 0 #quantidade atual de elementos
    
    def inserir(self, elemento):
        if self.tamanho < self.capacidade:
            self.dados[self.tamanho] = elemento #o novo elemento é armazenado na posição atual da lista (self.dados), no índice self.tamanho
            self.tamanho += 1 #Depois de inserir o elemento, aumenta o contador tamanho, já que agora há mais um elemento na lista
        else:
            print("Lista cheia")

    def inserir_em(self, indice, elemento):
        if self.tamanho >= self.capacidade:
            print("Lista cheia")
            return
        if indice < 0 or indice > self.tamanho:
            print("Índice inválido")
            return

        for i in range(self.tamanho, indice, -1):
            self.dados[i] = self.dados[i - 1]

        self.dados[indice] = elemento
        self.tamanho += 1
    
    def remover (self, indice):
        if 0 <= indice < self.tamanho: # Tem que ser menor que self.tamanho (ou seja, dentro da faixa de elementos válidos)
            for i in range(indice, self.tamanho -1): #Esse laço desloca os elementos à direita para a esquerda, a partir do índice onde o elemento foi removido
                self.dados[i] = self.dados[i + 1] #Move o elemento da posição seguinte (i + 1) para a posição atual (i), preenchendo o espaço deixado pela remoção
            self.dados[self.tamanho - 1] = None #Depois de deslocar os elementos, o último elemento da lista agora está duplicado e precisa ser apagado
            self.tamanho -= 1 #Diminui o contador de tamanho, ja que um elemento foi removido
        else:
            print("Indice invalido")
    
    def buscar (self, elemento): 
        for i in range(self.tamanho):
            if self.dados[i] == elemento: #comparando para saber se e isso que eu quero
                return i #retorna o indice do elemento encontrado
        return -1 #Elemento não encontrado
    
    def imprimir(self):
        for i in range(self.tamanho):
            print(self.dados[i], end ="|")
        print()

