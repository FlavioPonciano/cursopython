# Introdução ao desempacotamento + Tuples (Tuplas)

# Desempacotar (Retirar itens e transformar em variáveis)

# Caso tenha mais valores que variáveis ele vai mostrar erro e ao contrário também.

nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes
print(nome2)


nome4, nome5, nome6 = ['José', 'Fulano', 'Cicrano']
print(nome5)

# Pegando um valor e o restante empacotando e jogar em outra variável
# Se a variávei for utilizada ela geralmente leva nome de resto, se ela não for utilizada ela recebe um "_"
nome7, *_ = ['Antonia', 'Antonio', 'Julia']
print(nome7, _)
