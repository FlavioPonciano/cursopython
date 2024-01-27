# Exercicios com funções:

# Crie uma função que multiplica todos os argumentos não nomeados recebidos, retorne o total para uma variavel e mostre o valor da variável


def multplica(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

multiplicacao = multplica(10, 5)
print(multiplicacao)

# Crie uma função que fala se o um número é par ou impar. Retornar se o valor é par ou impar.
def par_impar(numero):
    verificador = numero % 2 == 0

    if verificador:
        return f'{numero} é par.'
    return f'{numero} é impar.'

print(par_impar(2))
print(par_impar(3))

