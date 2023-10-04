"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutáveis)
"""
nome = "Felicity Jones"
noutra_variavel = nome
nome = "Felicity Stone"
print(nome)
print(noutra_variavel)

lista_a = ["Oliver Queen", "Bruce Wayne", "Peter Parker", 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = "Clark Kent"
print(lista_a)
print(lista_b)
