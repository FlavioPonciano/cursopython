"""
Métodos Uteis:
append - Adiciona um item ao final
insert - Adiciona um item no indice escolhido
pop    - Remove do final ou do indice escolhido
del    - Apaga um indice
clear  - Limpa a lista
extend - Extende a lista 
+      - Concatena listas 
"""

lista = [10, 20, 30, 40]

# Adiciona o item de acordo com o indice solicitado, não é bom utilizar com listas muito grandes
# Primeiro argumento é o indice e o segundo é o valor que será adicionado (podendo ser qualquer tipo de dado).
lista.insert(0, 5)
print(lista)

# Ao tentar acessar um indice maior ou menor que a lista tem, ele vai gerar um erro.

# Tentar adicionar o valor no ultimo indice (mesmo sem saber qual é) ele vai adicionar ao próximo indice do ultimo criado. Mesmo adicionando, esse indice solicitado não será criado.
lista.insert(50, 12)
print(lista)