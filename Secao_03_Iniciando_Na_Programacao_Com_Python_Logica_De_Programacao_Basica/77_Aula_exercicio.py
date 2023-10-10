"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DÍGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.: 746.824.890-70 (746824890)
    11 10  9  8  7  6  5  4  3  2
*
    7  4   6  8  2  4  8  9  0  7 <-- PRIMEIRO DÍGITO
    77 40  54 64 14 24 40 36 0  14

Somar todos os resultados:
    77 + 40 + 54 + 64 + 14 + 24 + 40 + 36 + 0 + 14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
cpf = '746.824.890-70'
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')
cpf = cpf[:9]

soma = 0

for indice, valor in enumerate(cpf):
    if valor.isdigit():
        soma += int(valor) * (11 - indice)
        print(f'{valor} * {11 - indice} = {int(valor) * (11 - indice)}')

print(f'Soma: {soma}')

soma *= 10
print(f'Soma * 10: {soma}')

resto = soma % 11
print(f'Resto: {resto}')

if resto > 9:
    resto = 0
print(f'Resto: {resto}')

if resto == int(cpf[-1]):
    print('CPF válido')
else:
    print('CPF inválido')
