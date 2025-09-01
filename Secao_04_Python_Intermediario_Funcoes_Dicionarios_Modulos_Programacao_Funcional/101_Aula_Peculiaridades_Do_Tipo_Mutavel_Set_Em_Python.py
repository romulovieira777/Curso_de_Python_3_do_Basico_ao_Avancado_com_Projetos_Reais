# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()
print(s1)
print(s1, type(s1))

s2 = set('Felicty')
print(s2)

s3 = {'Felicty', 1, 2, 3, 4, 5, 5, 5, 5}
print(s3)

s4 = set() # Vazio
s5 = {'Felicty'}  # Com Dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

s6 = {1, 2, 3, 3, 3, 3, 3, 1}
print(s6)

l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s7 = set(l1)
l2 = list(s7)
print(l2)

s8 = set('Felicitty')
print(s8)

s9 = {1, 2, 3, 3, 3, 3, 3, 1}
print(3 not in s9)

for numero in s9:
    print(numero)
