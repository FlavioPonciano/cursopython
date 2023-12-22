# Operador lógico "not"
# usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

# Se a senha for diferente mostrar senha incorreta.
if senha != '123456':
    print('Senha incorreta.')

if not senha:
    print('Você não digitou nada!')


print(not True) #False
print(not False) # True