# main

from sys import path

import aula99_package.modulo # importando o modulo
from aula99_package.modulo import soma_do_modulo # importando apenas a soma ou a função necessária
from aula99_package import modulo # outra forma de importar o módulo
from aula99_package.modulo import * # importa todas as funções do módulo (se torna uma má prática pois perde rastreio de onde vem a função)

# print(*path, sep='\n')
print(aula99_package.modulo.soma_do_modulo(1, 2))
print(soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)

