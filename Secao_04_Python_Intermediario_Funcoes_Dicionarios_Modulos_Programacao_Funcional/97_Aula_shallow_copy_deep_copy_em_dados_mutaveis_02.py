# Keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - apaga um item com a chave especificada (del)
# popitem - apaga o último item adicionado
# update - atualiza um dicionário com outro dicionário ou com um iterável de pares
p1 = {
    'nome': 'Felicity',
    'sobrenome': 'Smoke',
}

print(p1['nome'])
print(p1.get('nome', 'Não existe!'))

nome = p1.pop('nome')
print(nome)
print(p1)

ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)

p1.update({
    'nome': 'Angelina',
    'sobrenome': 'Jolie',
    'idade': 40
})

print(p1)

p1.update(nome='Bruce', idade=50)
print(p1)

tupla = ('nome', 'Oliver'),
p1.update(tupla)
print(p1)

lista = [['nome', 'Oliver'], ['idade', 32]]
p1.update(lista)
print(p1)
