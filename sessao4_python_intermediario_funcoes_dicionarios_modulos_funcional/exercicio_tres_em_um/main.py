# Exercícios
from dados import produtos
from modulos import copia_profunda, aumenta_precos, nome_crescente, nome_decrescente, preco_crescente, preco_decrescente

print('Lista original')
print(*produtos, sep='\n')
print()

# Gere novos_produtos por deep copy (cópia profunda)
lista_acrescimo = copia_profunda(produtos)
# Aumente os preços dos produtos a seguir em 10%
aumenta_precos(lista_acrescimo)

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
lista_nome_crescente = copia_profunda(produtos)

nome_crescente(lista_nome_crescente)

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
lista_nome_decrescente = copia_profunda(produtos)
# Ordene os produtos por nome decrescente (do maior para menor)
nome_decrescente(lista_nome_decrescente)


lista_preco_crescente = copia_profunda(produtos)
# Ordene os produtos por preco crescente (do menor para maior)
preco_crescente(lista_preco_crescente)

lista_preco_decrescente = copia_profunda(produtos)
preco_decrescente(lista_preco_decrescente)
