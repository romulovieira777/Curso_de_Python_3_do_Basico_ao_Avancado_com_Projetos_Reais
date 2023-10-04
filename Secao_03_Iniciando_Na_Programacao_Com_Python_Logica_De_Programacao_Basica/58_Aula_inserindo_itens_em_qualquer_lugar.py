"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - Índices e fatiamento
Métodos úteis:
    append - Adiciona um item no ao final da lista
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - Limpa a lista
    extend - Estende a lista
    + - Concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#         0   1   2   3   4   5
lista = [10, 20, 30, 40, 50, 60]
lista.append('Felicty Smoak')
nome = lista.pop()
del lista[-1]
lista.clear()
lista.insert(0, 5)
lista.insert(2, 'Felicty Smoak')
print(lista, nome)
