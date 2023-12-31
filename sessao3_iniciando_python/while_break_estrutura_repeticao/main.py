"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim.
"""
condicao = True
while condicao:
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break # break dentro de um laço ela busca o while mais próximo, em caso de um laço dentro de outros laços
print('Acabou')
