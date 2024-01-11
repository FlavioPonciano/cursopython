# Lista de listas e seu índices

salas = [
    # 0        1
    ['Maria', 'Helena'], # 0
    # 0
    ['Elaine', ], # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)] # 2
]

print(salas) # Acessando a lista
print(salas[1][0]) # Acessando o valor da lista dentro da lista
print(salas[2][2])
print(salas[2][3][2]) # Acessando o valor dentro da tupla que está dentro da lista que está dentro de outra lista

print('#' * 15)

# for interno, o for maior faz a parte de fora e o for menor faz o interno e assim por diante.

for sala in salas:  
    print(f' A sala é {sala}')
    for aluno in sala:
        print(aluno)