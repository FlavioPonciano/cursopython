# Exibir os indices de uma lista

lista = ['Maria', 'Helena', 'Luiz']

indice = -1

for item in lista:
    indice += 1
    print(indice, item)

# Resolução professor

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])