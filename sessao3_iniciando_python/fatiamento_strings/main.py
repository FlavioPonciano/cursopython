"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::] i-inicio f-fim p-passo
Obs.: a função len retorna a quantidade de caracteres da string
"""

variavel = "Olá mundo"
print(variavel[4:])
print(variavel[4:7]) # pegar 1 a mais do que estou pedindo o indice final não é incluido
print(variavel[:5])
print(variavel[-8:-2])

# Função len conta os caracteres das strings
print(len(variavel))
print(len(variavel[3]))

# Utilizando passo
print(variavel[0:len(variavel):2]) # Passo de quantos em quantos ele tem que pegar os caracteres da string
print(variavel[::-1]) # Passo negativo ele faz a contagem de tras pra frente, nesse caso utilizando passo -1 ele inverte a string

print(variavel[-1:-10:-1]) # da mesma forma
