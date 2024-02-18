# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Flávio'}
]

for item in lista:
    if isinstance(item, set): # perguntar se um item é uma instancia de set como no exemplo
        print('SET')
        item.add(5) # se o item for set ele vai adicionar algo nesse item, nem todos os tipos tem a propriedade add.
        print(item, isinstance(item, set)) # Mostrando somente os itens set

    elif isinstance(item, str):
        print('STR')
        print(item.upper()) # O vscode consegue identificar o tipo que está sendo filtrado e mostra as opções que podems ser utilizdas com cada tipo de dado

    # Procurando mais de um tipo de item, nesse caso ele é um ou ou int ou float
    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)
    
    else:
        print('OUTRO')
