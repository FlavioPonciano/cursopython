"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extenmd, +
"""

#         01234
#        -54321
string = 'ABCDE' # 5 caracteres (len)
forma_criar_lista = list() # Não é a forma mais comum
# Se a letra estiver vazia ela consta como False

#         0     1           2            3    4
#        -5    -4          -3           -2   -1   
lista = [123, True, 'Flávio Alexandre', 1.2, []]

print(lista, type(lista))
print(lista[2].upper(), type(lista[2]))

lista[-3] = 'Logan'
print(lista[2])
print(lista)
