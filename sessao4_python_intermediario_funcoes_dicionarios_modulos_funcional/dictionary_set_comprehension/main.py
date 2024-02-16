# Dictionary Comprehension e Set Comprehesion

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'escritorio'
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor # ele vai colocar em letra maiuscula se o valor for str se não mantém o valor
    for chave, valor
    in produto.items()
}

# assim também pode ser feito:
dc = {
    chave: valor
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor
    in produto.items()
    if chave != 'categoria' # se a chave for diferente de categoria adiciona dentro do novo dicionário
}

print(dc)

# Posso transformar listas que parece dicionários em dicionários:
lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

# posso tanto fazer com comprehension:
dcl = {
    chave: valor
    for chave, valor in lista
}

print(dcl)

# Mas é muito mais simples utilizar o dict(), para lista que parecem ter chave e valor
print(dict(dcl))

# set comprehension
s1 = {i for i in range(10)}
print(s1)

# mas também poderia utilizar:
print(set(range(10)))

# Podendo também receber operações
s1 = {2 ** i for i in range(10)}
print(s1)
