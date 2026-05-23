class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        super().apresentar()
        print(f"Minha matrícula é {self.matricula}.")

aluno1 = Aluno("João", 20, "12345")
aluno1.apresentar()


'''A classe Pessoa é a classe base, e a classe Aluno é a classe derivada que herda os atributos e métodos da classe Pessoa.
A função super() é usada para chamar o método apresentar() da classe base (Pessoa) dentro do método apresentar() da classe derivada (Aluno),
 permitindo que o aluno se apresente usando as informações da pessoa e, em seguida, adicione informações adicionais sobre a matrícula.
A herança é um dos pilares da programação orientada a objetos, permitindo que classes compartilhem atributos e métodos, promovendo a reutilização de código e
 a criação de hierarquias de classes.

A classe Pessoa tem um método apresentar() que exibe o nome e a idade da pessoa. A classe Aluno herda esse método e o estende para incluir a matrícula do aluno.
Exemplo de uso:
aluno1 = Aluno("João", 20, "12345")
aluno1.apresentar()

Saída: Olá, meu nome é João e tenho 20 anos.
Minha matrícula é 12345.

A herança é um conceito fundamental na programação orientada a objetos que permite criar novas classes com base em classes existentes, promovendo a reutilização de código
 e a criação de hierarquias de classes.
A classe base (ou superclasse) é a classe que é herdada, enquanto a classe derivada (ou subclasse) é a classe que herda os atributos e métodos da classe base.
 A classe derivada pode adicionar novos atributos e métodos ou modificar os existentes para se adequar às suas necessidades específicas.
A função super() é usada para chamar métodos da classe base dentro da classe derivada, permitindo que a classe derivada aproveite a funcionalidade da classe base e,
 ao mesmo tempo, adicione ou modifique comportamentos conforme necessário.
'''