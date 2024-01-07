lista_compras = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    # Validação da opção
    if opcao != 'i' and opcao != 'a' and opcao != 'l':
        print('Opção inválida!')
        continue
    
    # Adicionar itens
    if opcao == 'i':
        item_adicionado = input('Digite o item: ')
        lista_compras.append(item_adicionado)
        print('Item adicionado!')
    
    # Listar itens com indices
    if opcao == 'l':
        if lista_compras == []:
            print('Lista vazia, adicione para mostrar itens.')
        else:
            for indice, item in enumerate(lista_compras):
                print(indice, item)

    
    # Apagar itens da lista
    if opcao == 'a':
        if lista_compras == []:
            print('Lista vazia, não é possível apagar.')
        else:
            for indice, item in enumerate(lista_compras):
                print(indice, item)
        
        apaga_item = input('Selecione o indice a ser apagado: ')

        try:
            apaga_indice = int(apaga_item)
            print(f'{lista_compras[apaga_indice]} apagado da lista')
            lista_compras.pop(apaga_indice)
        except:
            input('Item não encontrado!')
            continue
