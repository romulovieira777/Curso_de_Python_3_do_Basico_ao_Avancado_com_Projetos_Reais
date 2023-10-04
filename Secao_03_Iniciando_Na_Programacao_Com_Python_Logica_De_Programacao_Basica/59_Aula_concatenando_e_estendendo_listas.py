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
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_a)
print(lista_b)
print(lista_c)
print(lista_d)
