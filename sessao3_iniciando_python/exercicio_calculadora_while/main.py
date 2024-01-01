# Calculadora com While

print('*** Calculadora ***')



recebe_operador = ''
resultado = 0
while recebe_operador != 'sair':
    print('Escolha um operador "+" "-" "*" "/" "//" "**" "%"')
    print('Ou "sair" para finalizar.')
    recebe_operador = input('Digite o operador ou "sair": ')
    if recebe_operador == 'sair':
        print('Calculadora finalizada!')
        break
    
    recebe_primeiro_numero = input('Digite primeiro número: ')
    recebe_segundo_numero = input('Digite segundo número: ')

    primeiro_numero = int(recebe_primeiro_numero)
    segundo_numero = int(recebe_segundo_numero)

    if recebe_operador == '+':
        resultado = primeiro_numero + segundo_numero

    elif recebe_operador == '-':
        resultado = primeiro_numero - segundo_numero
    
    elif recebe_operador == '*':
        resultado = primeiro_numero * segundo_numero

    elif recebe_operador == '/':
        resultado = primeiro_numero / segundo_numero
    
    elif recebe_operador == '//':
        resultado = primeiro_numero // segundo_numero

    elif recebe_operador == '**':
        resultado = primeiro_numero ** segundo_numero

    elif recebe_operador == '%':
        resultado = primeiro_numero % segundo_numero
        
    else: 
        print('Operador inválido')
        break
    
    print(f'O resultado do calculo {primeiro_numero} {recebe_operador} {segundo_numero} = {resultado}')