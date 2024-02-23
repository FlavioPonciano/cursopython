import importlib # importando uma biblioteca que pode recarregar o módulo

import aula98_m

print(aula98_m.variavel)

for i in range(10):
    print(i)
    import aula98_m # módulo é singleton ele só vai ser importado uma vez independente de quantas vezes for chamado.s
    importlib.reload(aula98_m) # recarregando o módulo utilizando o importlib se não ele carrega somente uma vez por padrão

print('Fim')