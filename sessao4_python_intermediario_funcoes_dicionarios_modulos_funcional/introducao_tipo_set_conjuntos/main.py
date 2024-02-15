# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

s1 = {1, 2, 3, 3, 3, 3, 1}
print(s1) # mostrando apenas os valores sem repetições

# Transformando uma lista em conjunto para retirar os duplicados
l1 = [1, 2, 3, 3, 3, 1]
s2 = set(l1)
print(s2)
l2 = list(s2)
print(l2)

# not in, in:
print(2 not in s1) 
print(3 in s1)

# utilizando o for
for numero in s1:
    print(numero)



# Métodos úteis:
# add, update, clear, discard
    
s1 = set()
s1.add('Flávio') # add aceita apenas um valor por vez
s1.add(1)

s1.update('Olá mundo') # assim ele passa iteravel, letra por letra
s1.update(('Olá mundo',)) # passando um iteravel em si ele vai receber como uma coisa só no caso um tupla
s1.update((1, 2, 3, 4))
print(s1)

# s1.clear() # limpa o set
# print(s1)

# discart discarta apenas um valor
s1.discard('Olá mundo')
s1.discard(1)
print(s1)


print("#" * 20)
# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}

# União
s3 = s1 | s2
print(s3)

# Intersecção
s3 = s1 & s2
print(s3)

# Diferença que mostra o item que contém apenas no set da esquerda no primeiro
s3 = s1 - s2
print(s3)
s3 = s2 - s1
print(s3)

# Diferença simetrica, mostra os itens que estão presentes somente em um dos conjuntos
s3 = s1 - s2
print(s3)