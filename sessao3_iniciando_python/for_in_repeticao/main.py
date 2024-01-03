texto = 'Python'

novo_texto = ''

# 'letra' é criado por mim mesmo, eu mesmo passo para o for onde quero que ele jogue o elemento.
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')