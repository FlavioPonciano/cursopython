# count é um iterador sem fim - count está no módulo itertools

from itertools import count
# count entega o valor e soma +1
c1 = count(step=8, start=8) # recebe inicio e step se não utilizar keywords (count não recebe fim)
r1 = range(8, 100, 8) # range recebe inicio, fim e step

print('c1', hasattr(c1, '__iter__')) # verificando se o count é um iterável
print('c1', hasattr(c1, '__next__')) # verificando se o count um iterator

print('count')
for i in c1:
    if i > 100:
        break
    print(i)

print('range')
for i in r1:
    print(i)
