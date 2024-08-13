# Keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - apaga um item com a chave especificada (del)
# popitem - apaga o último item adicionado
# update - atualiza um dicionário com outro dicionário ou com um iterável de pares
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

d2 = d1.copy()

d2['c2'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)
