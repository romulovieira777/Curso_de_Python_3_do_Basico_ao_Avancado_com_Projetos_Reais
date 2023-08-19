nome = "Felicty Smoak"
altura = 1.75
peso = 85
imc = peso / altura ** 2

linha_1 = 'nome tem altura de altura'
linha_2 = f'{nome} tem {altura:.2f} de altura'
linha_3 = f'pesa {peso} quilos e seu IMC é'
linha_4 = f'{imc:.2f}'

# f-strings
print(f"{nome} tem {altura} de altura,")
print(f"pesa {peso} quilos e seu IMC é")
print(f"{imc}")

print(linha_1)
print(linha_2)
print(linha_3)
print(linha_4)
