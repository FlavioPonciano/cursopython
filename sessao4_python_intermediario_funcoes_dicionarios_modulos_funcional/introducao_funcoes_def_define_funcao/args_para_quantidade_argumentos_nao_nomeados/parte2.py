# return vai retornar um valor que vai ser armazenado em uma variável nesse caso:

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total
    
soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

# Há uma função pronta no Python que faz o mesmo que o código acima, também passando uma tupla:
print(sum((1, 2, 3, 4, 5, 6, 7, 8)))

# Aqui eu tenho uma tupla:e
numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# Para passare argumentos como valores eu preciso desempacotar eles utilizar "*" 
outra_soma = soma(*numeros) 
print(outra_soma)

print(*numeros) # desempacotando os números de dentro da tupla por isso eu não posso passar os valores dentro de sum sem ser uma tupla, pois ele vai reconhecer que são argumentos diferentes ao invés de valores para serem trabalhados.

# Como "numeros" é um iteravel (já é uma tupla) ele vai ser utilizado normalmente no sum
print(sum(numeros))
 