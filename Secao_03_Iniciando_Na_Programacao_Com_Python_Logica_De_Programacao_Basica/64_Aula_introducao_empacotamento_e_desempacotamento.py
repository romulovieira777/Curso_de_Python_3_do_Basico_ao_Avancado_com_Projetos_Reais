"""
Introdução ao desempacotamento + tuples (tuplas)
"""
nomes = ['Felicity', 'Angelina', 'Joana']
nome1, nome2, nome3 = nomes
print(nomes)
print(nome1)
print(nome2)
print(nome3)

nome1, *resto = ['Felicity', 'Angelina', 'Joana']
print(nome1, resto)


nome1, *_ = ['Felicity', 'Angelina', 'Joana']
print(nome1)

_, nome2, *_ = ['Felicity', 'Angelina', 'Joana']
print(nome2)

_, _, nome3, *resto = ['Felicity', 'Angelina', 'Joana']
print(nome3, resto)
