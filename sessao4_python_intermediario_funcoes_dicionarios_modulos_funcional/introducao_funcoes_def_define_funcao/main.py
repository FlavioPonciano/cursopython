"""
Introdução as Funções (def) em Python
Funções são trechos de código usado para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetro (argumentos) e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# Criando uma função:
# def Print():
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# (a, b, c) são chamados parametros, o valor que eles vão receber são chamados argumentos
def imprimir(a, b, c):
    print(a, b, c)

# Aqui são os argumentos que os parametros a, b e c vão receber
imprimir(1, 2, 3)

# A cada chamada os paramêtros podem ser mudados pelos argumentos
imprimir(4, 5, 6)

# Posso pré-definir um valor para os parametros
def saudacao(nome = 'Sem nome'):
    print(f'Olá, {nome}!')

    
saudacao('Flávio')
saudacao('Alexandre')

