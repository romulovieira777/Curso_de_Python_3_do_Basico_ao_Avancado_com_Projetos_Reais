"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um por vez
next -> me entregue o próximo valor
iter -> me entregue um iterador
"""
texto = 'Felicty'   # iterável
iterador = iter(texto)  # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break


for letra in texto:
    print(letra)
