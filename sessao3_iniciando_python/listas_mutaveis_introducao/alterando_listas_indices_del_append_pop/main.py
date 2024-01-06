# Métodos úteis: 
#     append, insert, pop, del, clear, extend, +
# Create Read Update Delete (CRUD)
# Criar, ler, alterar, apagar = lista[i] (CRUD)

# O mais interessante em lista é alterar o fim dela, para que o processamento não seja tão grande alterar ou excluir.

# Criar lista
lista = [10, 20, 30, 40]
print(lista)

# Alterar lista
lista[2] = 300
print(lista)

# Apagar elemento lista
del lista[1]
print(lista)

# Adicionando item ao final da lista (Não requer tanto processamento)
lista.append(50)
print(lista)

# Removendo o ultimo item da lista, eu posso pegar esse ultimo valor com o pop e ver o que foi removido, caso tenha mais um de um pop apenas o ultimo vai armazenar o valor em caso de chamada ao final.
ultimo_valor = lista.pop() 
print(lista, 'Removido', ultimo_valor)

# Removendo um item de acordo com o indice dele
lista.pop(1)
print(lista)