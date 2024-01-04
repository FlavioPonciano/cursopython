palavra_secreta = 'python'
palavra_secreta_mostrando = ''

recebe_letra = input('Digite apenas uma letra: ')

for recebe_letra in palavra_secreta:
    palavra_secreta_mostrando += '*'

if recebe_letra in palavra_secreta:
    palavra_secreta_mostrando += recebe_letra.index(recebe_letra)

print(palavra_secreta_mostrando)