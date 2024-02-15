# Exemplo de uso do set

letra = set()
while True:
    recebeLetra = input('Digite uma letra: ')
    letra.add(recebeLetra.lower())

    if 'l' in letra:
        print('Parabéns!')
        break

    print(letra)
print(letra)

