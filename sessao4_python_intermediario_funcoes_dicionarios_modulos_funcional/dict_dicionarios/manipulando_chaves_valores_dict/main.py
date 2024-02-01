# Manipulando chaves e valores em dicionários
pessoa = {}

# Adicionando uma chave com valor dentro do dict
pessoa['nome'] = 'Flávio Alexandre'



print(pessoa)
print(pessoa['nome'])

# Posso criar chaves dinamicamente também, essas chaves podem ser criadas tanto após quanto antes do dicionário.
chave = 'nome2'

# atribuindo a chave dinamica ao dict com valor
pessoa[chave] = 'Luiz Otavio'
print(pessoa[chave])

# Posso alterar o valor da chave também
pessoa[chave] = 'Fulano'
print(pessoa)

# Posso apagar uma chave também
del pessoa['nome2']
print(pessoa)

#  if não cancela uma exeção em caso de chave não existe, então podemos utilizar um método chamada get que retorna None se a chave não existir
print(pessoa.get('nome2', None))

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['nome2'])


