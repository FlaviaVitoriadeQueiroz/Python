#classes são modelos para criar objetos, ou seja, estruturas que combinam dados (atributos) e comportamentos (métodos).
class Pessoas: #class e a palavra-chave usada para definir uma classe
    def __init__(self, nome, idade): #__init__ e o método especial chamado construtor: executa quando o objeto é criado, self referência ao próprio objeto (obrigatório em métodos de instância)
        self.nome = "Vitoria" #atributo sao variáveis que pertencem ao objeto (como nome e idade)
        self.idade = 19 

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

#Criando um objeto em uma classe
p1 = Pessoas("Maria", 25)
p1.apresentar()
print(p1.nome)