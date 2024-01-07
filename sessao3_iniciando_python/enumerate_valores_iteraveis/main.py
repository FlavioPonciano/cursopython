# Enumerate - enumera iteráveis (indices)

lista = ['Maria', 'Helena', 'Luiz']

# lista_enumerada = enumerate(lista)  # Não se é utilizado o enumerate em variável, geralmente se utiliza direto no for ou converter ela em uma tupla ou lista
# lista_enumerada = list(enumerate(lista, start=0)) # Posso dar uma parametro de start

# for item in enumerate(lista):
#     print(item)

# Para separar o item do indice pode-se usar um for, de cada item dentro da lista com enumerate eu pego dois itens sendo o primeiro o indice e o segundo o item em si.
for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

print('#' * 15)

# Outra forma de se fazer essa divisão entre item e indice, é jogar ambos dentro do for antes do in, assim ele vai fazer um for dentro do for e trazer ambos:
    
for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice]) # Além de mostrar o indice e o item, também pode fazer utilizando lista[indice], mas deixando somente indice e o nome já aparece ambos.