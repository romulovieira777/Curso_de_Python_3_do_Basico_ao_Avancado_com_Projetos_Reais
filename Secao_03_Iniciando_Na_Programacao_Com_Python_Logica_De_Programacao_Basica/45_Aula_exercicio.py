"""
Construir uma calculadora usando o while
"""
while True:
    sair = input('Deseja sair? [s]im ou [n]ão: ').lower().strip()
    if sair == 's':
        break
    elif sair == 'n':
        ...
    else:
        print('Digite apenas [s] ou [n]')
        continue

    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operador == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    elif operador == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    elif operador == '/':
        print(f'{num1} / {num2} = {num1 / num2}')
    else:
        print('Operador inválido.')
        continue

    print()

print('Até a próxima!')
