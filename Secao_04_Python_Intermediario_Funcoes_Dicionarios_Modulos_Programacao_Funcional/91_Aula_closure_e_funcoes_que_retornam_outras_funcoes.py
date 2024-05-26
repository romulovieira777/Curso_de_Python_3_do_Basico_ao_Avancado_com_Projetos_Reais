"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}'
    return saudar()


s1 = criar_saudacao('Bom dia', 'Luiz')
s2 = criar_saudacao('Boa tarde', 'João')

print(s1)
print(s2)


def criar_saudacao_(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}'
    return saudar


s1 = criar_saudacao_('Bom dia', 'Luiz')
s2 = criar_saudacao_('Boa tarde', 'João')

print(s1())
print(s2())


def criar_saudacao_01(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar


falar_bom_dia = criar_saudacao_01('Bom dia')
falar_bom_tarde = criar_saudacao_01('Boa tarde')

print(falar_bom_dia('Luiz'))
print(falar_bom_tarde('João'))


for nome in ['Luiz', 'Maria', 'João']:
    print(falar_bom_dia(nome))
    print(falar_bom_tarde(nome))
