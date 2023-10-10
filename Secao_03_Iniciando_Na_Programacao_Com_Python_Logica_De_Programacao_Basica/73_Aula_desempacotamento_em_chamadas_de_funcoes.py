"""
# Desempacotamento em chamadas
# de métodos e funções
"""
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    #  0           1
    ['Maria', 'Helena', ],  # 0
    #  0
    ['Elaine', ],  # 1
    #  0       1       2          3
    ['Luiz', 'Joana', 'Eduarda', (0, 10, 20, 30, 40)],  # 2
]

a, b, *_, c = lista

print(a, c)
print(*lista)
print(*string)
print(*tupla)
print(*salas, end='\n')
print(*salas, sep='\n')

for nome in lista:
    print(nome)

for nome in lista:
    print(nome, end=' ')
