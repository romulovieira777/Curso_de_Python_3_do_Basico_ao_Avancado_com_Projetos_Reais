# Conversação dos tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool


print(1 + 1)
print('a' + 'b')
#print('1' + 1)  # TypeError: can only concatenate str (not "int") to str
print('1', type('1'))
print(int('1'), type(int('1')))
print(int('1') + 1)
print(float('1.2') + 1)
print(type(float('1.2') + 1))
print(bool(' '))
print(str(11) + 'b')
