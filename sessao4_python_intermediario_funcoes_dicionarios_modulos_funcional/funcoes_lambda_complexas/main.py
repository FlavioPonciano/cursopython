# Funções lambda complexas (para entendimento)

def executa(funcao, *args):
    return funcao(*args)

# Converter essas funções em funções lambda
def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# Função soma:
print(
    executa(
        lambda x, y: x + y,
        2, 3
    ), # Essa função lambda é a mesma coisa que essas duas chamadas abaixo
    # executa(soma, 2, 3), # esse aqui não precisa
    # soma(2, 3) # esse aqui também não precisa
)

# Função de duplicar
duplica = executa(
    lambda m: lambda n: n * m,
    2
)

print(duplica(2))

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)