# split e join com list e str
# split - divide uma SyntaxWarning
# join - une uma string

frase = 'Olha só que, coisa interessante'
# Se não for colocado nenhum paramêtro no split ele vai separar a string por espaços.
lista_palavras = frase.split()
print(lista_palavras)

lista_frases = frase.split(",")
print(lista_frases)

# Cortando na virgula + o espaço
lista_frases = frase.split(", ")
print(lista_frases)

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip()) # strip corta os espaços do começo e do fim da string sendo rstrip() cortando o espaço da direita e lstrip() que corta os espaços da esquerda.

# Melhor forma de trabalhar frases com lista, pois mantém o dado original caso necessário
lista_frases_corrigida = []
for i, frase in enumerate(lista_frases):
    lista_frases_corrigida.append(lista_frases[i].strip())

print(lista_frases_corrigida)

# Da mesma forma funciona o join podendo unir dois iteraveis por espaço, simbolos ou virgula + espaço como no exemplo
frases_unidas = ', '.join(lista_frases_corrigida)
print(frases_unidas)