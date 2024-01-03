"""
Iterável -> str, range, etc (___iter___) método chamado iter
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entrega seu iterador
"""
# texto = iter('Luiz') #.__iter__()
# print(texto)
# print(next(texto)) #.__next__()
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto)) # ele levanta um erro para parar a iteração e avisar o for por exemplo que acabou a iteração

# Isso é a mesma coisa que for

texto = 'Luiz'
iterador = iter(texto) # iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

# É a mesma coisa que:
    for letra in texto:
        print(letra)