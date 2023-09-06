"""
Construir uma calculadora usando o while
"""
while True:
    sair = input('Deseja sair? [s]im ou [n]ão: ').lower().strip().startswith('s')

    if sair is True:
        break
