# Higher Order Functions - Funções de primeira classe

def executa(funcao, *args):
    return funcao(*args)

def saudacao(msg, nome):
    return f'{msg}, {nome}'


variavel = executa(saudacao, 'Bom dia', 'Flávio')
print(variavel)

print(executa(saudacao, 'Bom dia', 'Alexandre'))

