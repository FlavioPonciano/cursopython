# extend - Extende a lista 
# +      - Concatena listas 


# Concatenando duas ou mais listas
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)

# Extender a lista ele une a primeira com a segunda lista, o extend não retorna nada, então a mudança é na primeira lista.
lista_a.extend(lista_b)
print(lista_a)