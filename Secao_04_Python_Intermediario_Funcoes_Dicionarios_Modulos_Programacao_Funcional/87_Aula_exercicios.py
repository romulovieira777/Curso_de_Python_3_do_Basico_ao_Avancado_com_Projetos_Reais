# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplica_1_2_3 = multiplica(1, 2, 3)
print(multiplica_1_2_3)


# Crie uma função fala se um número é par ou ímpar usando todos os argumentos não nomeados recebidos.
# Retorne se o número é par ou ímpar.

def par_ou_impar(*args):
    for numero in args:
        if numero % 2 == 0:
            print(f"{numero} é par")
        else:
            print(f"{numero} é ímpar")


par_ou_impar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def par_ou_impars(numero):
    if numero % 2 == 0:
        return "Par"
    return "Ímpar"


print(par_ou_impars(2))
