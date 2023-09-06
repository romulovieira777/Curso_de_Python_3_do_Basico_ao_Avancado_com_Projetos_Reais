"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador_01 = 0

while contador_01 <= 10:
    contador_01 += 1
    print(contador_01)

    if contador_01 == 4:
        break

print('Acabou!')

contador_02 = 0

while contador_02 <= 100:
    contador_02 += 1

    if contador_02 == 6:
        print('Não vou mostrar o 6.')
        continue

    if 10 <= contador_02 <= 27:
        print(f'Não vou mostrar o, {contador_02}.')
        continue

    print(contador_02)

    if contador_02 == 40:
        break

print('Acabou!')
