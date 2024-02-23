# Package

# utilizando o __all__ quando a importação for de tudo com o '*' ele vai enviar apenas o que está dentro do all
__all__ = [
    'variavel',
    'soma_do_modulo'
]

variavel = 'Alguma coisa'

def soma_do_modulo(x, y):
    return x + y

# Se uma nova variável for adicionada e não for adicionada no all ela não será importada pelo import *
nova_variavel = 'ok' 
