# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
import sys

platform = 'A MINHA' # Aqui acaba sobreescrevendo devido a palavra da variável ser a mesma
print(sys.platform)
print(platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
from sys import exit, platform

print(platform)

# Pode adicionar um apelido ao módulo e chamar ele por outro nome, mas isso não é muito indicado.
# alias 1 - import nome_modulo as apelido
import sys as s

sys = 'alguma coisa'
print(s.platform)              
print(sys)


# alias 2 - from nome_modulo import objeto as apelido
from sys import exit as ex
from sys import platform as pf

print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo e acaba deixando meio obscuro de onde vem as funcionalidades
from sys import *

print(platform)
exit()