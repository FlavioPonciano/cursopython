# Mais sobre iterables e iterator (iteraveis e iteradores)
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# Havendo mais chamadas do que o tamanho do iteravel ele vai chamar um StopIteration