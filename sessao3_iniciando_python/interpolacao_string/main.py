"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
#interpolar utilizar % e a letra referente as descritas acima, utilizando % após aspas
variavel = '%s, o preço total foi R$:%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (15, 15)) # %4x onde o 4 é o número de casas do hexadecimal geralmente sendo utilizado 4 e 8

