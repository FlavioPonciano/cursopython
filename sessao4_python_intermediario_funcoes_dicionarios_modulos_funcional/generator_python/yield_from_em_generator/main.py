# Yield from

def gen1():
    print('Começou gen1')
    yield 1
    yield 2
    yield 3
    print('Acabouou gen1')

def gen3():
    print('Começou gen3')
    yield 10
    yield 20
    yield 30
    print('Acabouou gen3')
# Posso indicar um if dentro do generator para indicar a sua execução:
def gen2(gen=None):
    print('Começou gen2')
    if gen is not None:
        yield from gen 
    yield 4
    yield 5
    yield 6
    print('Acabouou gen2')

# Chamando direto pela chamada da função na variável
g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2() # Nesse caso como ele segue con None ele vai executar apenas o que está dentro do gen2

for numero in g1:
    print(numero)

print("#" * 30)

for numero in g2:
    print(numero)

print("#" * 30)

for numero in g3:
    print(numero)