# Gerando um CPF qualquer com random

import random

#Posso adiconar esse programa todo dentro de um for maior e gerar uma quantidade infinita de cpf:
for _ in range(100):
    cpf = ''

    # Para cada casa em um tamanho de 9, gerar um número aleatório
    for i in range(9):
        cpf += str(random.randint(0, 9))

    calculo = 0
    contador = 10

    for numero in cpf:
        calculo += int(numero) * contador
        contador -= 1

    penultimo_digito = (calculo * 10) % 11
    penultimo_digito = penultimo_digito if penultimo_digito <= 9 else 0


    cpf_com_penultimo = cpf + str(penultimo_digito)
    calculo = 0
    contador = 11

    for numero in cpf_com_penultimo:
        calculo += int(numero) * contador
        contador -= 1

    ultimo_digito = (calculo * 10) % 11

    ultimo_digito = ultimo_digito if ultimo_digito <= 9 else 0

    cpf_final = cpf_com_penultimo + str(ultimo_digito)
    print(cpf_final)
