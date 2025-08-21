class Aluno:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo 

#Criando um objeto em uma classe
aluno1 = Aluno("Gabriel", 19, 'M')
aluno2 = Aluno("Maria", 18, 'F')

print(aluno1.nome)
print(aluno1.idade)


