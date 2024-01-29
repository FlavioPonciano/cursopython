# Execicios
# Crie Funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro

def recebe_numero(numero):
    def faz_conta(multiplicador):
      return numero * multiplicador
    return faz_conta

envia_numero = recebe_numero(2)

print(envia_numero(2))

for n in [2, 3, 4]:
   print(envia_numero(n))