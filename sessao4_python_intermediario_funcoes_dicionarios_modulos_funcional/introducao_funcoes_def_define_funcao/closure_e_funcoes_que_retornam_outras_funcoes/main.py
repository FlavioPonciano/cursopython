# Closure e funções que retornam outras funções

def cria_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

falar_bom_dia = cria_saudacao('Bom dia')
falar_boa_noite = cria_saudacao('Boa noite')

print(falar_bom_dia('Flávio'))
print(falar_boa_noite('Flávio'))

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))

 