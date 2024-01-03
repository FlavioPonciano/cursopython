"""
For + Range
range -> range(start, stop, step)
"""

# apenas um número no range ele vai apenas indicar o final (no caso sempre -1 pois começa em 0)
numeros = range(10)

# print(numeros) -- mostrar o range sempre precisar do for

# for pega o valor e não o indice 
# para cada valor em números nesse caso ele vai seguir o passo de 1 em 1 e o começo em 0 pois não foi indicado
for numero in numeros:
    print(numero)

print('*'*10)

# nessse caso ele começa em 5, termina em 10 e pula de 2 em 2
numeros = range(5, 10, 2)
for numero in numeros:
    print(numero)

print('*'*10)


# nesse caso ele começa em 5, termina em 10 e o passo é 1 pois não foi indicado
numeros = range(5, 10)
for numero in numeros:
    print(numero)

print('*'*10)

# range também tem negativo e pra isso preciso indicar o passo negativo e os demais também
    
numeros = range(0, -10, -1)
for numero in numeros:
    print(numero)