# __init__

# print('Você importou', __name__)

# def dobra(x):
#     return x * 2

from modulos_package.modulo_a import nova_variavel, variavel, soma_do_modulo

# no init é um dos poucos casos onde se pode utilizar o import * - pois ele auxiliaria em caso de alteração de nome de função ou de adição de novas funções
from modulos_package.modulo_a import *
from modulos_package.modulo_b import *