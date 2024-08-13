# Exercício - Sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

respostas_certas = 0

for pergunta in perguntas:
    print(f"\n{pergunta['Pergunta']}")

    for i, opcao in enumerate(pergunta['Opções']):
        print(f"{i}) - {opcao}")

    resposta = input('Sua resposta: ')

    if resposta == pergunta['Resposta']:
        respostas_certas += 1

print(f"\nVocê acertou {respostas_certas} respostas.")
