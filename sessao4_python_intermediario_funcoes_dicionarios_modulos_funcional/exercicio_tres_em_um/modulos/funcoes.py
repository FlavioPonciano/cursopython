import copy

# Cria uma cópia profunda do que é enviado
def copia_profunda(origem):
    return copy.deepcopy(origem)

# Aumenta em 10% os preços passados
def aumenta_precos(novos_valores):
    novos_valores = [
        {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
        for produto in novos_valores
    ]
    print('Valores atualizados:')
    print(*novos_valores, sep='\n')
    print()

# Ordena o nome em ordem crescente
def nome_crescente(nova_ordem):
    nova_ordem.sort(key=lambda item: item['nome'])
    print('Ordem atualizada')
    print(*nova_ordem, sep='\n')
    print()

# Ordena o nome em ordem decrescente
def nome_decrescente(nova_ordem):
    nova_ordem.sort(key=lambda item: item['nome'], reverse=True)
    print('Ordem atualizada')
    print(*nova_ordem, sep='\n')
    print()

# Ordena o preço por ondem crescente
def preco_crescente(nova_ordem):
    nova_ordem.sort(key=lambda item: item['preco'])
    print('Ordem atualizada')
    print(*nova_ordem, sep='\n')
    print()

# Ordena o preço por ondem decrescente
def preco_decrescente(nova_ordem):
    nova_ordem.sort(key=lambda item: item['preco'], reverse=True)
    print('Ordem atualizada')
    print(*nova_ordem, sep='\n')
    print()