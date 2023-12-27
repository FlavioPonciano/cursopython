"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o número que você digitar: ')

# esse formato é apenas para demonstrar, não é o mais indicado
# o try vai tentar realizar a ação desejada e caso não finalize ele joga para except
try:
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O Dobro de {numero_str} é {numero_float * 2:.2f}')
# except vai sinalizar o erro conforme indicado
except:
    print('Isso não é um número.')