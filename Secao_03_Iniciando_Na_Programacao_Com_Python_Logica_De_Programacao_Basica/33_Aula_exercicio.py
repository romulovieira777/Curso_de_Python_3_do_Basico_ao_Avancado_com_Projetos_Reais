"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou impar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""
number = input('Digite um número inteiro: ')

if number.isdigit():
    number = int(number)
    if number % 2 == 0:
        print(f'{number} é par!')
    else:
        print(f'{number} é impar!')
else:
    print('Isso não é um número inteiro!')


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
