# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Flávio Alexandre',
    'sobrenome': 'Ponciano'
}

# Posso utilizar as duas formas de saber a quantidade de chaves dentro do dicionário:
print(pessoa.__len__())
print(len(pessoa))

# Não há problema em ter dados iguais em dicionário, porém somente o ultimo valor será usado.

# Retorna um dict_keys
print(pessoa.keys())
# Esse dict key eu posso fazer a coerção em Tupla ou Lista e utilizar esses valores
print(tuple(pessoa.keys()))
print(list(pessoa.keys()))

# Utilizando o for ele vai retornar as chaves e não o valor precisa do pessoa[chave] para chammar o valor
for chave in pessoa:
    print(chave, pessoa[chave])

# Trazendo somente aos valores
print(list(pessoa.values()))
# Posso utilizar o for com values
for valor in pessoa.values():
    print(valor)


# Itens vem chave e valor com dict_items trazendo um tupla com chave e valor
print(list(pessoa.items()))

# Da mesma forma se pode usar com items trazendo a chave o valor de forma separada
for chave, valor in pessoa.items():
    print(chave, valor)
    
# no caso de o dicionário solicitando não vier com uma chave especifica, podemos configurar um valor padrão para essa chave: 
pessoa.setdefault('idade', 0)
# o valor informado vai ser setado na chave que será criada, nesse valor o nome da chave sendo idade e o valor de 0, mas caso a chave idade venha com o dicionário e com um valor, esse sedefault não vai fazer nenhum alteração
print(pessoa['idade'])

