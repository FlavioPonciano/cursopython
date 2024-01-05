import os

palavra_secreta = 'aluno'
recebe_palavra = ''
tentativas = 0
while True:
    recebe_letra = input('Digite apenas uma letra: ')
    tentativas += 1
    if len(recebe_letra) > 1:
        print('DIGITE APENAS UMA LETRA!!')
        continue

    if recebe_letra in palavra_secreta:
        recebe_palavra += recebe_letra
    print(recebe_palavra)
    print(f'{tentativas} tentativa(s)')

    forma_palavra = ''
    for letra in palavra_secreta:
        if letra in recebe_palavra:
            forma_palavra += letra
        else:
            forma_palavra += '#'
    
    if forma_palavra == palavra_secreta:
        os.system('cls')
        print(f'Parabéns a palavra secretá é "{palavra_secreta}" com {tentativas} tentativas!')