# if  / elif       / else
# se / se nao se  / senao

entrada = input('Você que "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Bem vindo ao sistema.')
elif entrada == 'sair':
    print('Saindo do sistema.')
else:
    print('O sistema não entendeu o que você digitou.')

print('FORA DOS BLOCOS.')
