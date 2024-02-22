# raise - lançando exceções (erros)

# print(123)
# #lançando um erro:
# raise ValueError('Deu erro')
# print(456)

# def divide(n, d):
#     try: # posso usar um try dentro de um try
#         return n / d
#     except ZeroDivisionError:
#         print('__________')
#         raise # relançando um erro

# print(divide(8, 0))

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Voce está tentando dividir por zero.') # criando meu próprio erro.
    
def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float'
            f'"{tipo_n.__name__}" enviado'    
        )


# o erro tem que ser tratado fora da função
def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero()
    return n /d

print(divide(8, '0'))