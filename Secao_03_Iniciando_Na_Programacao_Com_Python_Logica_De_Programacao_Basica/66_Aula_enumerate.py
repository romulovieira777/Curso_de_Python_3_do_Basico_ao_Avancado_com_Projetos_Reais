"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Felicity', 'Angelina', 'Joana']
lista.append('Tony Stark')

lista_enumerada = enumerate(lista)
print(lista_enumerada, type(lista_enumerada))
print(next(lista_enumerada))

for item in lista_enumerada:
    print(item)

print('O que tem na lista enumerada?', lista_enumerada)
# -------------------------------------------------------

lista = ['Felicity', 'Angelina', 'Joana']

for item in enumerate(lista):
    print(item)
# -------------------------------------------------------

lista = ['Felicity', 'Angelina', 'Joana']
lista_enumerada = list(enumerate(lista))

for item in lista_enumerada:
    print(item)
# -------------------------------------------------------
lista = ['Felicity', 'Angelina', 'Joana']
lista_enumerada = list(enumerate(lista, start=5))

for item in lista_enumerada:
    print(item)
# -------------------------------------------------------
lista = ['Felicity', 'Angelina', 'Joana']

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)
# -------------------------------------------------------
lista = ['Felicity', 'Angelina', 'Joana']

for indice, nome in enumerate(lista):
    print(indice, nome)
# -------------------------------------------------------
lista = ['Felicity', 'Angelina', 'Joana']

for tupla_enumerada in enumerate(lista):
    for valor in tupla_enumerada:
        print(valor)
# -------------------------------------------------------
lista = ['Felicity', 'Angelina', 'Joana']

for tupla_enumerada in enumerate(lista):
    print("For da tupla:", tupla_enumerada)
    for valor in tupla_enumerada:
        print(f"\t{valor}")
# -------------------------------------------------------
lista = ['Felicity', 'Angelina', 'Joana']

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])
