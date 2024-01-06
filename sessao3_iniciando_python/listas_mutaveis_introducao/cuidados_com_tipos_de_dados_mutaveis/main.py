# Cuidados com dados mutáveis
# = - copiado o valor (imutáveis)
# = - aponta para o mesmo valor na memória (mutáveis)


lista_a = ['Luiz', 'Maria']
# Apontando para o mesmo lugar na memória
lista_b = lista_a # Para copiar e não ser afetada pelas alterações na outra lista pode utilizar lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_b)