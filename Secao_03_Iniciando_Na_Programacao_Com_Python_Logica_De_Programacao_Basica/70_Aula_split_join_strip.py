"""
split e join com list str
split - divide uma string
join - une uma string
"""
frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split()
lista_frases = frase.split(',')

for i, frase in enumerate(lista_frases):
    print(f'{i} - {frase.strip()}')
    print(lista_frases[i].strip())

for i, frase in enumerate(lista_frases):
    lista_frases[i] = lista_frases[i].strip()

print(lista_palavras)
print(lista_frases)

# ---------------------------------------------------------

frases = 'Olha só que, coisa interessante'
lista_frases_cruas = frases.split(',')

lista_frases_1 = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases_1.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases_1)

# ---------------------------------------------------------

frases = 'Olha só que, coisa interessante'
lista_frases_cruas = frases.split(',')

lista_frases_1 = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases_1.append(lista_frases_cruas[i].strip())

frases_unidas = '-'.join(lista_frases_1)
print(frases_unidas)
