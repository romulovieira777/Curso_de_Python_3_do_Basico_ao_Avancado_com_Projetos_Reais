# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
# p y t h o n
# -6 -5 -4 -3 -2 -1

nome = 'Python'

print(nome[2])
print(nome[-4])
print('y' in nome)
print('z' in nome)
print('Pyt' in nome)
print('0' in nome)
print(10 * '-')
print(10 not in nome)
print('0' not in nome)


nome_1 = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome_1:
    print(f'Encontrei {encontrar} em {nome_1}.')
else:
    print(f'Não encontrei {encontrar} em {nome_1}.')
