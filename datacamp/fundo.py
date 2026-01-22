class Informacoes:
    def __init__(self):
        self.nome = 'Flávia Vitória de Queiroz'
        self.formacao = 'Data Science'
        self.instituicao = 'UFMS'

    def exibir(self):
        print(f'Nome: {self.nome}')
        print(f'Formacao: {self.formacao}')
        print(f'Instituicao: {self.instituicao}')

if __name__ == '__main__':
    info = Informacoes()
    info.exibir()

