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


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hour = input('Digite um horário (0-23): ')

if hour.isdigit():
    hour = int(hour)
    if hour < 0 or hour > 23:
        print('Horário deve estar entre 0 e 23!')
    else:
        if hour <= 11:
            print('Bom dia!')
        elif hour <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print('Por favor, digite um horário entre 0 e 23.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
name = input('Digite seu primeiro nome: ')

if len(name) <= 4:
    print('Seu nome é curto!')
elif len(name) <= 6:
    print('Seu nome é normal!')
else:
    print('Seu nome é muito grande!')
