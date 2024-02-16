# List comprehension com mais de um for

# lista = []
# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))

# Com list comprehension
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

lista = [
    [letra for letra in 'Luiz'] # para cada x é gerado uma nova lista
    for x in range(3)
]

print(lista)