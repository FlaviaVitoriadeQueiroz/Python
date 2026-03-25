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
            self.fim = (self.fim + 1) % self.tamanho  # comportamento circular
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
        
    def consultar(self):
        if self.quantidade > 0: #verifica se a fila n esta vazia, pq n da ver oq n existe
            return self.dados[self.inicio] #retorna o que estiver no inicio
        else:
            print("Erro: Fila vazia.")
            return None

    def contar(self):
        return self.quantidade 
    
#menu
def mostrar_menu():
    print("\n=== MENU DA FILA ===")
    print("1. Enfileirar elemento")
    print("2. Desenfileirar elemento")
    print("3. Consultar primeiro elemento")
    print("4. Contar elementos")
    print("0. Sair")

def main(): #para caso o valor inserido seja invalido
    try:
        tamanho = int(input("Informe o tamanho da fila: "))
    except ValueError:
        print("Entrada inválida. Usando tamanho padrão 5.")
        tamanho = 5

    fila = Fila(tamanho)

    while True: #Cria um loop infinito, para que o menu continue sendo mostrado até o usuário escolher sair, pq sem criterio sera sempre verdade
        mostrar_menu() #esta chamando a funcao menu
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            elemento = input("Digite o elemento a enfileirar: ")
            fila.enfileirar(elemento) #chama a funcao 
        elif opcao == "2":
            fila.desenfileirar() #chama a funcao
        elif opcao == "3":
            primeiro = fila.consultar() #chama a funcao
            if primeiro is not None:
                print(f"Primeiro elemento: {primeiro}")
        elif opcao == "4":
            print(f"Quantidade de elementos na fila: {fila.contar()}") #chama a funcao
        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__": #Esse trecho faz com que a função main() seja executada somente quando o arquivo é rodado diretamente, e não quando importado em outro arquivo.
    main()