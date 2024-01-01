# While/Else

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1

# Caso tenha algum break dentro do while o else não será executado.
else:
    print('Não encontrei um espaço na string')
print('Fora do while')