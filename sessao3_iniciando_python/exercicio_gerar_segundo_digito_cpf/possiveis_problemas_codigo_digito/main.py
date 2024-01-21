# Caso o cliente envie o cpf com ponto e traço. Nesse caso posso utilizar o replace:
# cpf_completo = '746.824.890-70'.replace('.', '') \
#     .replace('-', '') \
#     .replace(' ', '')

# Também posso utilizar expressão regular:
# Importando módulo de regular expression import re
import re 
import sys
entrada = input('CPF[746.824.890-70]:')
cpf_completo = re.sub( # chamando re.sub de substituição
    r'[^0-9]', # Expressão pegando tudo que não for um número
    '', # Substituindo por nada
    entrada
)

# Verificando número repetido do cpf
# entrada é igual a primeiro caractere da entrada repetido pelo tamanho da entrada
entrada_sequencial = entrada == entrada[0] * len(entrada)
if entrada_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit # sys sai do python
cpf = cpf_completo[:9]
calculo = 0
contador = 10

for numero in cpf:
    calculo += int(numero) * contador
    contador -= 1

penultimo_digito = (calculo * 10) % 11
penultimo_digito = penultimo_digito if penultimo_digito <= 9 else 0

# --- Calculo segundo Digito ---
cpf_com_penultimo = cpf + str(penultimo_digito)
print(cpf_com_penultimo)
calculo = 0
contador = 11

for numero in cpf_com_penultimo:
    calculo += int(numero) * contador
    contador -= 1

ultimo_digito = (calculo * 10) % 11

ultimo_digito = ultimo_digito if ultimo_digito <= 9 else 0

cpf_final = cpf_com_penultimo + str(ultimo_digito)
print(cpf_final)

valida_cpf = 'CPF válido' if cpf_completo == cpf_final else 'CPF inválido'
print(valida_cpf)