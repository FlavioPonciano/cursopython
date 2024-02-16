# Mapeamento de dados em list comprehension
# Pegando dados de um iterável e transformando ou não mas colocando em outra lista
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    #produto['nome']
    # {'nome': produto['nome'], 'preco': produto['preco']} # desempacotando chave por chave
    {**produto, 'preco': produto['preco'] * 1.05} # desempacotando toda a lista para realizar as alterações
    if produto['preco'] > 20 else {**produto} # Condicional utilizada para fazer mapeamento, nesse caso se o produto for maior que 20 ele vai fazer a linha superior e adiconar 5% de aumento e caso seja menor que 20 ele vai manter o valor.
    for produto in produtos
]

print(*novos_produtos, sep='\n')