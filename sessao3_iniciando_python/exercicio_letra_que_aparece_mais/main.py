frase = 'O Python é uma linguagem de programação multiparadigma.'\
    'Python foi criado por Guido van Rossum.'

i = 0
contador_letra = 0
contador_letra_mais_vezes = 0
letra_atual = ''
letra_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    contador_letra = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if contador_letra_mais_vezes < contador_letra:
        contador_letra_mais_vezes = contador_letra
        letra_mais_vezes = letra_atual

    i += 1

print(f'A letra que mais apareceu foi "{letra_mais_vezes}" aparecendo {contador_letra_mais_vezes}')