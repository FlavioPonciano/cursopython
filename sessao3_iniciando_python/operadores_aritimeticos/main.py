# Operadores aritiméticos em Python

adicao = 10 + 10
print('Adição:', adicao)

subtracao = 10 - 5
print('Subtração:', subtracao)

multiplicacao = 10 * 10
print('Multiplicação:', multiplicacao)

divisao = 10 / 2.2 # sempre vai retornar um float
print('Divisão', divisao)

divisao_inteira = 10 // 2.2 # retorna um resultado int ou caso tenha float ele vai retornar um número float ele vai retornar .0 apenas.
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação:', exponenciacao)

modulo = 55 % 2 # resto da divisão
print('Módulo:', modulo)

print(10 % 8 == 0) # se 10 é divisivel por 8 ele retorna 0 e assimm ele vai retornar True
print(16 % 8 == 0) # se 16 é divisivel por 8
print(10 % 2 == 0) # Se um número é par basta verificar se o resto da divisão do número por 2 é igual a 0
print(15 % 2 == 0) # resto 1 ou outro número ele não é par