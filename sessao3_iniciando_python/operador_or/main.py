# Operadores lógico
# and(e) or(ou) not(não)
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro, a expressão inteira será avalidada naquele valor.
# São considadores falsy (que você já viu) 0, 0.0, '', False
# Também existe o tipo None que é usado para representar um não valor.

entrada = input('[E]ntrar [S]air: ') 
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# uma expressão com and e or pode ficar ambigua, podemos utilizar parenteses para ditar a precedencia. 
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')



#Avaliação de curto circuito
print(True or False)
print(False or 0 or 'abc')

senha = 0 or False or 0 or 'abc' or True
print(senha)

#Se o input estiver vazio ele vai avaliar como False e passar a próxima que a 'Sem senha' que é True
senha = input('Senha: ') or 'Sem senha'
print(senha)