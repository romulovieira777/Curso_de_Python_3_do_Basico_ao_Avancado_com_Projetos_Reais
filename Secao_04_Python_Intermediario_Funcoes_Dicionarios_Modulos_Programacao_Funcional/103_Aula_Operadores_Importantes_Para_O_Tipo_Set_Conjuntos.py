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

# Métodos úteis:
# add, update, clear, discard

s10 = set()
s10.add('Felicity')
s10.add(1)
s10.update('Olá mundo!')
s10.update(('Hello World!', 1, 2, 3, 4, 5))
s10.clear()
s10.discard('Felicity')  # Não dá erro se o valor não existir
s10.discard(1)
print(s10)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s11 = {1, 2, 3}
s12 = {2, 3, 4}
s13 = s11 | s12
print(s13)

s14 = s11 & s12
print(s14)

s15 = s11 - s12
print(s15)

s16 = s11 ^ s12
print(s16)
