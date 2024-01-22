"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o paramêtro, o valor padrão será usado.
"""

# Posso ter um parametro que pode ou não ser enviado, posso utilizar o None como argumento para que eu consiga condicionar um código e mostrar ou utilzar o z se ele for 0 por exemplo.
def soma(x, z=None, y=0): # Todo argumento com valor padrão, todo próximo argumento precisa também ter valor padrão
    if z is not None:
        print(f'{x=} y={y} {z=}', x+y+z)
    else:
        print(f'{x=} {y=}', x+y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)