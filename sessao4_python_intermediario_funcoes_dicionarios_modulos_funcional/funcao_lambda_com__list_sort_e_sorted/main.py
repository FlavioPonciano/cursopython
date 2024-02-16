# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True) # Ordena sua lista
# sorted(lista) # Cria uma nova lista ordenada com uma cópia rasa 

#Porém o Python não consegue por ele mesmo ordenar uma lista por itens dentro de dicionários que estão denteo dessa lista
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# Podemos utilizara uma função para ensinar o Pythonb a fazer essa ordenação:
def ordena(item):
    return item['nome'] # dentro da lista ele vai buscar a chave "nome" e ordenar utilizando a tabela unicode UTF-8
    
# key é uma função tem que ser uma definição de função sem executar (sem "()")
lista.sort(key=ordena) # então lista vai receber os itens em ordem contendo uma lista com dicionários ordenados

#Posso retornar, printar ou printar com for para deixar mais ordenado
for item in lista:
    print(item)

print("#" * 20)

lista2 = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def exibir(lista2):
    for item in lista2:
        print(item)
    print()

# Fazendo a mesma função acima porém em apenas uma linha utilizando lambda
lista2.sort(key=lambda item: item['nome'])

# Posso utilizar com sorted e outros:
l1 = sorted(lista2, key=lambda item: item['sobrenome'])

# Posso fazer uma função que vai me exibir os valores e chamar ela
exibir(l1)
