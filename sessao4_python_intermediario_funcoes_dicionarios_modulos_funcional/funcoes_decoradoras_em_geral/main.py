# Funções Decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Altertar
# Funções decoradoras são funções que decoram outras funções.
# Decoradores são usados para fazer o Python usar as funções em outras funções.

# Essa aqui é uma função decoradora:
def cria_funcao(func):
    def interna(*args, **kwarg):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwarg)
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora você foi decorada.')
        return resultado
    return interna

def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')


inverte_string_checando_parametro = cria_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)