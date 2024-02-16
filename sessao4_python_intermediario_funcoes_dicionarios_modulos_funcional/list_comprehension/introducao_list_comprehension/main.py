# List comprehension em Python
# List Comprehension é uma forma rápida de criar listas a partir de iteráveis.
# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
#print(lista)

# à esquerda do for eu posso indicar o que quero adicionar, por exemplo uma string, uma letra qualquer. Ou qualquer lógica, como uma ternário, um filtro
lista = [
    numero * 2
    for numero in range(10)
]
print(lista)