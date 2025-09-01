# Exemplo de uso dos sets em Python

letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra)

    if 'l' in letras:
        print('Parabéns você ganhou! 🎉')
        break

    print(letras)
    print(f'Tamanho do set: {len(letras)}')
