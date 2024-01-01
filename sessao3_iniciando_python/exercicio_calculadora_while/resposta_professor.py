# Calculadora com while

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    # Flag para verificar se os números são válidos
    numeros_validos = None

    num_1_float = 0
    num_2_float = 0

    # Tentando fazer a conversão e conseguindo a Flag recebe True
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    # Caso não consiga fazer a conversão a Flag mantém o status none (adicionado ao except apenas como segurança,)    
    except:
        numeros_validos = None

    # Condição para números inválidos na Flag com None, utilizando o "continue" para retornar ao inicio do código
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    # Verificando se tem algum dos operadores permitidos digitado pelo usuário
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    # Verificando se o usuário não digitou mais de um caractere por engano
    if len(operador) > 1:
        print('Digite apenas um operador')

    if operador == '+':
        print(f'{num_1_float} + {num_2_float}= ', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float}= ', num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float}= ', num_1_float * num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float}= ', num_1_float / num_2_float)
    else:
        print('O código não deve chegar até aqui.')

    # Utilizando lower() para deixar a letra minuscula e startwith() para verificar se a primeira coisa digitada é o s (se ocorrer tudo certo ele vai atribuir True a variável que vai ser verificada no próximo if)
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break