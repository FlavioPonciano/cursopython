nome = input('Qual o seu nome? ') #vai ser sempre no tipo string a não ser que faça a coerção
print(f'O seu nome é {nome=}') #colocando sinal de igual depois do nome da variável ele vai pegar o nome e o valor da variável.

numero_1 = input('Digite um número: ')
# numero_1 = int(input('Digite um número: ')) fazendo a coerção direto no input, mas isso não é uma boa forma de se fazer
numero_2 = input('Digite outro número: ')

int_numero1 = int(numero_1)
int_numero2 = int(numero_2)

print(f'A soma dos números é: {int_numero1 + int_numero2}')
