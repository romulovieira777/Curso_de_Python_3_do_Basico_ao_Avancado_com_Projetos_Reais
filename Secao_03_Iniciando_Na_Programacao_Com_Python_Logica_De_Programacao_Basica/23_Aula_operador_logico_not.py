# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if senha == '123456':
    print('Acesso permitido.')
else:
    print('Senha incorreta.')


# Usando o operador lógico "not"
if not senha != '123456':
    print('Senha incorreta.')


# Usando o operador lógico "not"
if not senha:
    print('Você precisa digitar uma senha.')


print(not True)
print(not 0)
print(not 1)
