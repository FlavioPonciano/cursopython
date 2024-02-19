# Generator expression, Iterables e Iterators em Python

import sys # importar o módulo sys tem um método que pode mostrar o tamanho dos elementos na memória.

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
lista = [n for n in range(10000)]
# ao invés de utilizar [] se utiliza () para fazer o generator, como abaixo:
generator = (n for n in range(10000))
print(sys.getsizeof(lista)) # o tamanho da lista acaba sendo muito maior do que do generator
print(sys.getsizeof(generator)) # o generator acaba mantendo o seu tamanho salvo independente da quantidade de dados, pois ele está pausado na primeira execução
print(next(generator)) # ele vai atribuindo o valor um por um
print(next(generator))
print(next(generator))

# podendo fazer até um for para trazer os valores:
for n in generator:
    print(n)
