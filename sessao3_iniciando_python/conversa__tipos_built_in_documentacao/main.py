"""
https://docs.python.org/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

# string imutável
string = 'luiz Otávio' # este valor é imutável não consigo alterar o valor
outra_variavel = f'{string[:3]}' # para "mudar" é necessário atribuir em uma nova variável

print(string)
print(outra_variavel)
print(string.capitalize()) # primeira letra maiúscula
print(string.zfill(100)) # preeche o restante da string com 0 a esquerda

# Pesquisar outras funcionalidades na documentações do python