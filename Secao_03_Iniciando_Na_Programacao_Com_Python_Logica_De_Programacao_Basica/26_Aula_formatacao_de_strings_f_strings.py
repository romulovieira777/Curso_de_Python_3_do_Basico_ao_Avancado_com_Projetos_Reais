"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal (ABCDEF0123456789)
(Caractere) (><^) (Quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r __repr__ !s __str__ !a __asc__
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746}')
print(f'{1000.4873648123746:.1f}')
print(f'{1000.4873648123746:,.1f}')
print(f'{-1000.4873648123746:-,.1f}')
print(f'{1000.4873648123746:+,.1f}')
print(f'{1000.4873648123746:0>+10,.1f}')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
