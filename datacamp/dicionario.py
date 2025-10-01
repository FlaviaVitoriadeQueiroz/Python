#exercicio 1
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
europe ['italy'] = 'rome'

print('italy' in europe)

#adicionando polonia
europe ['poland'] = 'warsaw'

print(europe)

#exercicio 2
europe1 = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

#atualizando a capital da alemanha
europe1 ['germany'] = 'berlin'

# Removendo australia
del(europe1['australia'])

print(europe1)

#exercicio 3
europe2 = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

print(europe2['france'])

#criando um dicionario 
data = {'capital': 'rome', 'population': 59.83}

#adicionando italia, com o dicionario data sendo seu valor
europe2 ['italy'] = data

print(europe2)