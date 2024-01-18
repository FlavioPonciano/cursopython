"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# --- Calculo primeiro Digito ---
cpf_completo = '32751362087'
cpf = cpf_completo[:9]
calculo = 0
contador = 10

for numero in cpf:
    calculo += int(numero) * contador
    contador -= 1

penultimo_digito = (calculo * 10) % 11
penultimo_digito = penultimo_digito if penultimo_digito <= 9 else 0

# --- Calculo segundo Digito ---
cpf_com_penultimo = cpf + str(penultimo_digito)
print(cpf_com_penultimo)
calculo = 0
contador = 11

for numero in cpf_com_penultimo:
    calculo += int(numero) * contador
    contador -= 1

ultimo_digito = (calculo * 10) % 11

ultimo_digito = ultimo_digito if ultimo_digito <= 9 else 0

cpf_final = cpf_com_penultimo + str(ultimo_digito)
print(cpf_final)

valida_cpf = 'CPF válido' if cpf_completo == cpf_final else 'CPF inválido'
print(valida_cpf)