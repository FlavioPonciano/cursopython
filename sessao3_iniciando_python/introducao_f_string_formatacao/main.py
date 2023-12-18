nome = 'Flávio Ponciano'
altura = 1.80
peso = 95
imc = peso / altura ** 2

# f-strings
#altura:.2f informa a quantidade de casas decimais depois do ponto
linha_1 = f"{nome} tem {altura:.2f} de altura"
linha_2 = f'pesa {peso} quilos'
linha_3 = f'Seu IMC é de:, {imc:.2f}'


print(linha_1)
print(linha_2)
print(linha_3)


valor = 1000.50
informa_valor = f'R$: {valor:,.2f} adiciona virgula em caso de valores, por exemplo'

print(informa_valor)