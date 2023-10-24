"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y):
    print(f'{x=} + y={y}', '|', 'x + y =', x + y)


soma(1, 2)
soma(y=2, x=1)


def soma_1(x, y, z):
    print(f'{x=} + y={y} + z={z}', '|', 'x + y + z =', x + y + z)


soma_1(y=1, z=2, x=3)
soma_1(1, 2, z=5)
