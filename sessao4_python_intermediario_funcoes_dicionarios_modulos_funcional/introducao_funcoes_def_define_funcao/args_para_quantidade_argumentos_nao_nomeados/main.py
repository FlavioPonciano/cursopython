"""
args - argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembre-te de desempacotamento:
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    print(args, type(args))
    total = 0
    for numero in args:
        print('Total', total, numero)
        total += numero
        print('Total', total)
    print(total)

soma(1, 2, 3, 4, 5, 6)