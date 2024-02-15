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

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda'
}

# Pegando valor de uma chave com método get
print(p1.get('nome'))
# Caso a chave não existe ele vai retornar None por padrão ou podendo passar um valor
print(p1.get('nome2'))

# pop atribui um valor à uma variável e exclui do dicionário
#nome = p1.pop('nome')

# popitem elimina a ultima chave do dicionário e também atribui ela à uma variável
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# update Atualiza o dicionário e criar novas chaves
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30
# })

# update também pode ser escrito assim:
# p1.update(nome='novo valor', idade=30)

# também posso passar os dados no update de tuplas e listas: Em caso de um item só é necessário deixar uma virgula sobrando
# tupla = (('nome', 'novo valor'), ('idade', 30))
tupla = [['nome', 'novo valor'], ['idade', 30]]
p1.update(tupla)
print(p1)