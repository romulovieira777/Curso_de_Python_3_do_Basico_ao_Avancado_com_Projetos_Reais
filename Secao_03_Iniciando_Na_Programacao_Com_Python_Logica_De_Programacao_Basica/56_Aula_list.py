"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - Índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#   +01234
#   -54321

string = 'ABCDE'    # 5 caracteres (len)

print(bool([]))

#          0     1        2            3     4
#         -5    -4       -3           -2    -1
lista = [123, True, 'Felicity Smoak', 10.5, []]
lista[-3] = 'Oliver Queen'

print(lista)
print(type(lista))
print(lista[2])
print(lista[-2])
print(lista[2], type(lista[2]))
print(lista[2].upper(), type(lista[2]))
