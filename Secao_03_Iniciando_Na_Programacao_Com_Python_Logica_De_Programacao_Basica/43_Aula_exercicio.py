"""
Iterando strings com while
"""


def adicionar_asteriscos(nome):
    nome_em_asteriscos = ""
    indice = 0

    while indice < len(nome):
        nome_em_asteriscos += nome[indice] + "*"
        indice += 1

    return nome_em_asteriscos[:-1]


nome = input("Digite um nome: ")
nome_com_asteriscos = adicionar_asteriscos(nome)
print(nome_com_asteriscos)
