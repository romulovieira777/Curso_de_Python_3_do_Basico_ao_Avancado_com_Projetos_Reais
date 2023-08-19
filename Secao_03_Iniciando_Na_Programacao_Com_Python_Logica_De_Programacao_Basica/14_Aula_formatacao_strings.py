# Exemplo de formatação de strings 1
a = 'A'
b = 'B'
c = 1.1
string = 'a={0} b={1} c={2:.2f}'
formato = string.format(a, b, c)
print(formato)


# Exemplo de formatação de strings 2
a = 'A'
b = 'B'
c = 1.1
string = 'b={nome2} a={nome1} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c)
print(formato)
