# if  / elif       / else
# se / se nao se  / senao

condicao = True

if condicao:
    print('Este é o dódigo dentro do if.')
else:
    print('Este é o código dentro do else.')

print('Este é o código fora do if.')

if 10 == 10:
    print('Outro if.')

print('Este é o código fora do outro if.')


condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('Código para condição 1.')
    print('Código para condição 1.')
elif condicao2:
    print('Código para condição 2.')
elif condicao3:
    print('Código para condição 3.')
elif condicao4:
    print('Código para condição 4.')
else:
    print('Nenhuma condição foi satisfeita.')
