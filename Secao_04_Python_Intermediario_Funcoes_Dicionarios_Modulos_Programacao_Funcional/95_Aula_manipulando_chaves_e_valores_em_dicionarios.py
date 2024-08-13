# Manipulando ochaves e valores em dicionários
pessoa = {}

chave = 'nome'

pessoa['nome'] = 'Felicity'
pessoa['sobrenome'] = 'Smoke'

print(pessoa[chave])

pessoa['nome'] = 'Angelina'

del pessoa['sobrenome']

print(pessoa['nome'])

print(pessoa.get('sobrenome'))

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])
