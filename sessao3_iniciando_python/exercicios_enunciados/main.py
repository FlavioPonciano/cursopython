"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
recebe_numero = input("Digite um número inteiro: ")
try:
    verificador_par = int(recebe_numero) % 2
    par_impar = 'par'
    if verificador_par:
        par_impar = 'impar'
    print(f'O número {recebe_numero} é {par_impar}')
except:
    print('Não é um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
recebe_hora = input('Qual a hora atual? ')
try:
    hora = int(recebe_hora)
    if hora >= 0 and hora <= 11:
        print(f'Bom dia! {hora} horas')

    elif hora >= 12 and hora <= 17:
        print(f'Boa tarde! {hora} horas')

    elif hora >= 18 and hora <= 23:
        print(f'Boa noite! {hora} horas')

    else: 
        print('Hora inválida!')
except:
    print('Não é um número válido')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ')

tamanho_nome = len(nome)
if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto.')

    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')

    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')