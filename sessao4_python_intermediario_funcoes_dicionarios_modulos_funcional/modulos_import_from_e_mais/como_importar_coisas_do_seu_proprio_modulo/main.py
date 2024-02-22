# Como importar coisas do seu próprio módulo (ponto de vista do __main__)

# importando tudo do módulo
import aula97_m
# importando partes do módulo
from aula97_m import variavel_modulo, soma

print('Este módulo se chama', __name__)
print(aula97_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula97_m.soma(2, 3))