"""
Iterando strings com While
"""

nome = input('Digite seu nome: ')

tamanho_nome = len(nome)

contador = 0
nome_estilo = ''
while contador < tamanho_nome:
    nome_estilo += f'*{nome[contador]}'
    contador += 1

print(f'{nome_estilo}*')