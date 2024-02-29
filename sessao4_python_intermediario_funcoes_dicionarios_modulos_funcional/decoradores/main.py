# Decoradores
# Decorar = Adicionar / Remover / Restringir / Altertar
# Decoradores são usados para fazer o Python usar as funções em outras funções.
# Decoradores são "Syntax Sugar" (Açucar sintático)

# Essa aqui é uma função decoradora:
def cria_funcao(func):
    def interna(*args, **kwarg):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwarg)
        resultado += 'Qualquer coisa' # Na chamada da função pelo @ ela também além de adicionar e remover eu também posso alterar o resultado
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora você foi decorada.')
        return resultado
    return interna # é retornada essa função, é alterada a função original 

# Utilizando o @ com a função acima da outra função ele transfere a decoração para essa função e retorna a clousure da função decoradora
@cria_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')


invertida = inverte_string('123')
print(invertida)