class No:
    def __init__(self,dados):
        self.dados = dados
        self.proximo = None #ponteiro para o próximo nó

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None #inicializa a cabeca de lista (a caixinha pequena) vazia

    def inserir_inicio(self, dado): #passa o dado que quer inserir como argumento
        novo_no = No(dado) #cria um novo no, passando o dado para ele
        novo_no.proximo = self.cabeca #faz o novo no apontar para a atual cabeca de lista
        self.cabeca = novo_no #atualiza a cabeca para apontar para o novo no

    def remove_inicio(self):
        if self.cabeca:
            self.cabeca = self.cabeca.proximo #atualiza a cabeca para apontar para o proximo no, removendo o primeiro, ja que em python a gestao de memoria e automatica

    def imprimir(self):
        atual = self.cabeca #criamos um objeto que aponta para quem a cabeca de lista aponta
        while atual: #enquanto n for nulo
            print(atual.dados, end=" -> ")
            atual = atual.proximo #atualiza o objeto para apontar para o proximo no
        print("None")
