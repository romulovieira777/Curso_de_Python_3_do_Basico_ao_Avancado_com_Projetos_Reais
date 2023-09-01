"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou impar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""
# Solution I
number = input('Digite um número inteiro: ')

if number.isdigit():
    number_int = int(number)
    par_impar = number_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {number_int} é {par_impar_texto}!')
else:
    print('Você não digitou um número inteiro!')

# Solution II
number = input('Digite um número inteiro: ')

try:
    number_int = int(number)
    par_impar = number_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {number_int} é {par_impar_texto}!')
except:
    print('Você não digitou um número inteiro!')
