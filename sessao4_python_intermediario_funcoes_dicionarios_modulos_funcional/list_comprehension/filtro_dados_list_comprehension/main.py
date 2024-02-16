# Filtro de dados em list comprehension

# pprint ajuda a mostrar de forma mais legivel que o print não consegue fazer, podendo criar uma função para utilizar esse módulo.
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto} 
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
    # antes do for é mapeamento e depois do for é filtro
    # nesse caso se preço do produto for maior à 10 e maior ou igual e os produtos com aummento de 5%
]

p(novos_produtos)
# print(*novos_produtos, sep='\n')
# p(novos_produtos)

# lista = [n for n in range(10) if n < 5] # if do filtro após o list comprehensin
# p(lista)

