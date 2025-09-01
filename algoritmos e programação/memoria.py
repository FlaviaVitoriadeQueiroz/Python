import array

#varaiveis simples
v = 18
y = v #y agora tem o valor de x
v = 9

print(f"v = {v}, y = {y}")

#variaveis compostas
arr1 = array.array('f', [3,6,9])
arr2 = arr1 #referencia, o segundo aponta para o primeiro
arr1[0] = 18

print(f"arr1 = {arr1}, arr2 = {arr2}") #como e uma referencia, ambos terao os mesmos valores

#objeto simples
class Pessoa:
    def __init__(self, nome): #metofo construtor
        self.nome = "Maria"

a1= Pessoa("Rafaela") #chamando o construtor e passando o nome de reafaela
a2 = a1 #e uma referencia e n uma variavel simples
a2.nome = "Vitoria"

print(f"a1 = {a1.nome}, a2 = {a2.nome}") #ambos teram o mesmo output

#identificadores
print(f"id(v) = {id(v)}, id(y) = {id(y)}, id(v) = {id(v)}")
print(f"id(arr1) = {id(arr1)}, id(arr2) = {id(arr2)}, id(arr1) = {id(arr1)}")
print(f"id(a1) = {id(a1)}, id(a2) = {id(a2)}, id(a2) = {id(a2)}")