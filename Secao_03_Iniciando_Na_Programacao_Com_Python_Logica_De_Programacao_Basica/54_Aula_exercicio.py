"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Qual o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
import random

# Lista de palavras secretas
palavras_secretas = ["python", "programacao", "openai", "inteligencia", "desenvolvimento"]

# Escolha aleatória de uma palavra secreta
palavra_secreta = random.choice(palavras_secretas)

# Inicialização de variáveis
palavra_adivinhada = ["*"] * len(palavra_secreta)
tentativas = 0
letras_digitadas = []


# Função para exibir o estado atual da palavra a ser adivinhada
def exibir_palavra():
    print("Palavra: " + " ".join(palavra_adivinhada))


# Loop principal do jogo
while True:
    exibir_palavra()
    letra = input("Digite uma letra: ").lower()

    # Verifica se a letra já foi digitada
    if letra in letras_digitadas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    letras_digitadas.append(letra)

    # Verifica se a letra está na palavra secreta
    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra_adivinhada[i] = letra
        print("Letra correta!")
    else:
        print("Letra incorreta. Tente novamente.")
        tentativas += 1

    # Verifica se o jogador adivinhou a palavra ou esgotou as tentativas
    if "".join(palavra_adivinhada) == palavra_secreta:
        print("Parabéns! Você adivinhou a palavra secreta: " + palavra_secreta)
        break
    elif tentativas >= 6:
        print("Suas tentativas acabaram. A palavra secreta era: " + palavra_secreta)
        break
