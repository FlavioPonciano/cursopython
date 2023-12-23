"""
Formatção básica de strings
s = string
d = int
f = float
.<número de digitos>f
x ou X = hexadecimal
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
= - força o número a aparecer antes dos zeros
Sinal = + ou - 
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
# largura fixa na viarável se ela não atingir a quantidade de caracteres
print(f'{variavel: >10}') # adicionar 10 espaços à esquerda
print(f'{variavel: <10}') # adicionar 10 espaços à direita
print(f'{variavel: ^10}') # centralizar a string 
print(f'{variavel:*^10}') # dá pra usar caracteres normais e especiais 

print(f'{1000.2983189643434634:+.1f}') # posso adicionar virgula para o milhar e tbm colocar o sinal de mais para ele mostrar quando o número for positivo ou negativo
print(f'{1000.2983189643434634:0=+10.1f}') # posso adicionar também casas a direita e a esquerda

print(f'O hexadecimal de 1500 é {1500:08X}')

print(f'{variavel!r}')