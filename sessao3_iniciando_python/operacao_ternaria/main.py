# Operação ternária (condional de uma linha) 
# <valor> if <condicao> else <outro valor>

print('Valor' if True else 'Outro valor')
print('Valor' if False else 'Outro valor')

condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

digito = 8
novo_digito = digito if digito <= 9 else 0
print(novo_digito)

novo_digito = 0 if digito > 9 else digito
print(novo_digito)

# Não recomendado utilizar:
print('Valor' if True else 'Outro valor' if True else 'Fim')
print('Valor' if False else 'Outro valor' if True else 'Fim')
print('Valor' if False else 'Outro valor' if False else 'Fim')