# Desempacotamento em chamadas de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# Pegando os elementos, em uma lista grande posso selecionar os que quero
primeiro, segundo, *resto, antepenultimo, ultimo = lista
# acompanhado do resto eu posso pegar os adjacentes tanto antes quanto depois dele
print(primeiro, ultimo, antepenultimo)

# Desempacotamento em chamadas de funções:

print(*lista)
print(*string)
print(*tupla)

salas = [
    # 0        1
    ['Maria', 'Helena'], # 0
    # 0
    ['Elaine', ], # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)] # 2
]

print(*salas)
print(*salas, sep='\n')

# Esse desempacotamento seria a mesma coisa que um for:
for nome in lista:
    print(nome, end=' ', sep='')