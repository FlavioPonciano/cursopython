"""
Exercicio:
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeiura letra do seu nome é {letra}
        A ultima letra do seu nome {letra}
Se nada for digitado em nome ou idade:
    Exiba: "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome completo: ')
idade = input('Digite a sua idade: ')


if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if " " in nome:
        print('Seu nome contém espaço.')
    else:
        print('Seu nome não contém espaço.')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')