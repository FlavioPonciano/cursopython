# # Exercício - Adiando execução de funções
# def soma(x, y):
#     return x + y


# def multiplica(x, y):
#     return x * y


# def criar_funcao(funcao, *args):
#     def adiciona_y(y):
#         return funcao(*args, y)
#     return adiciona_y


# soma_com_cinco = criar_funcao(soma, 5)
# print(soma_com_cinco(15))

# multiplica_por_dez = criar_funcao(multiplica, 10)
# print(multiplica_por_dez(12))

def criar_contador():
    count = 0  # Inicializa a variável count dentro da função externa

    def incrementar():  
        nonlocal count  # Define count como variável não local para que possa ser modificada pela função interna
        count += 1  # Incrementa a variável count em 1
        return count  # Retorna o valor atualizado de count
    
    def resetar():
        nonlocal count  # Define count como variável não local para que possa ser modificada pela função interna
        count = 0  # Reseta a variável count para 0
        return count  # Retorna o valor atualizado de count
    
    return incrementar, resetar  # Retorna as funções internas incrementar e resetar como uma tupla

# Criar um contador
incrementar, resetar = criar_contador()

# Testando as funções
print(incrementar())  # Saída: 1
print(incrementar())  # Saída: 2
print(resetar())      # Saída: 0
print(incrementar())  # Saída: 1
