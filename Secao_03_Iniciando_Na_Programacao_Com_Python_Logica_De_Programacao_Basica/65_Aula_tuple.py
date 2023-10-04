"""
Tipo tupla - Uma lista imutável
"""
nomes = ['Felicity', 'Angelina', 'Joana']
nomes[1] = 'Jolie'
_, _, nome, *resto = nomes
print(nome)
print(nomes)

nomes = 'Felicity', 'Angelina', 'Joana'
print(nomes[1])
print(nomes, type(nomes))


nomes = ('Felicity', 'Angelina', 'Joana')
print(nomes[1])
print(nomes, type(nomes))
