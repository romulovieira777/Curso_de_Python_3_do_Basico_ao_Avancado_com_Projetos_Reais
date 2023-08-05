# \r\n
# \n -> LF

print(12, 34)
print(56, 78)

print(12, 34, sep="")
print(56, 78, sep='')

print(12, 34, sep="-")
print(56, 78, sep='-')

print(12, 34, sep=" ", end="\r\n")
print(56, 78, sep=' ', end='\r\n')

print(12, 34, sep=" ", end="\n")
print(56, 78, sep=' ', end='\n')

print(12, 34, sep=" ", end="\n##")
print(56, 78, sep=' ', end='\n##')

print(12, 34, sep=" ", end="##\n")
print(56, 78, sep=' ', end='##\n')
