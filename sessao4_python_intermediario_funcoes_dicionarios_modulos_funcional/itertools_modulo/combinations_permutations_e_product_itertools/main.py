# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

# Uma função apenas para organizar o print das listas:
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliester']
]

print_iter(combinations(pessoas, 2)) # Passando o nome da lista e a quantidade de grupo
print_iter(permutations(pessoas, 2)) # Ele passa todas as combinações inclusive se sequencia, não levando em consideração a repetição dos dados
print_iter(product(*camisetas)) # Produto cartesiano, preciso desempacotar a lista para que ele itere dentro das listas dentro da lista