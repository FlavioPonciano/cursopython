# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


contador_acertos = 0
for pergunta in perguntas:
    print('Pergunga:', pergunta['Pergunta'])

    opcoes = pergunta['Opções']
    for indice, opcao in enumerate(opcoes):
        print(f'{indice}) {opcao}')
    resposta = pergunta['Resposta']
    
    recebe_opcao_usuario = input('Digite a opção: ')
    if recebe_opcao_usuario.isdigit():
        recebe_opcao_int = int(recebe_opcao_usuario)

    if opcoes[recebe_opcao_int] == resposta:
        print('Resposta correta! ✔')
        contador_acertos += 1
    else:
        print('Resposta incorreta! ❌')

print(f'{contador_acertos}/3 acertos')