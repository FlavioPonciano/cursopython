"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
#Posso importar um módulo chamado decimal
import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3) # imprecisão no resultado
print(f'{numero_3:.2f}') # formatando ele já ajusta o resultado para o mais correto possível

# arredondando a casa decimal, sendo o segundo atributo a quantidade de casas
print(round(numero_3, 2))

print('#' * 15)
# Geralmente utilizado com pontos flutuantes com muitas casas decimais, mas geralmente ele pede para colocar em string o valor
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)