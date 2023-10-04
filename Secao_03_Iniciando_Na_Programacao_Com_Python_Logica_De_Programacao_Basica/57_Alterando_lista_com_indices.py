"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - Índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#         0   1   2   3   4   5
lista = [10, 20, 30, 40, 50, 60]
numero = lista[2]
lista[2] = 300
del lista[2]
lista.pop(3)
lista.append(70)
lista.append(80)
lista.append(90)
ultimo_valor = lista.pop()
print(numero)
print(lista[2])
print(lista)
print(lista, 'Removido', ultimo_valor)
