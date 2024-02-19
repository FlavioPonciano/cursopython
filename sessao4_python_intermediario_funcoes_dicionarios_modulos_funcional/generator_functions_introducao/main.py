# Introdução as Generator functions em Python (função geradora)

def generator(n=0):
    yield 1 # pausa a execução da função, yield utilizado somente em generator, ele vai guardar o valor e aguardar o next
    print('Continuando...')
    yield 2 # Pausar
    print('Continuando...')
    yield 3
    print('Vou terminar')
    return 'Acabou' # return finalização a função (ele levanda uma exeção de stop iteration)

# gen = generator(n=0)
# print(next(gen)) # Posso chamar vez por vez de forma mais manual
# print(next(gen))

# Ou posso chamar de forma dinâmica utilizando o for:
gen = generator(n=0)
for n in gen:
    print(n)

# Lógica para criar um range de 10
def gerador(n=0, maximum=10):
    while True:
        yield n # função vai sempre de yield para outro yield
        n += 1
        # Para criar um range posso fazer o incremento e adicionar uma lógica para finalizar o generator para que ele não vire um loop infinito.
        if n >= maximum:
            return


gen2 = gerador(n=2, maximum=12)
for n in gen2:
    print(n)

