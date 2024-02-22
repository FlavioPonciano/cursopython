# try precisa de outro bloco

try:
    print('ABRIR ARQUIVO')
    8/0
# Posso ter ou não ter except com finally.
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Dividiu zero')
# Posso ter mais de um except também.
except IndexError as error:
    print('IndexError')
except(NameError, ImportError):
    print('NameError, ImportError')
# Else também é opcional com finally e o else é utilizado quando não há nenhum tipo de erro.
else:
    print('Não deu erro')

# finally é um  bloco que sempre será executado no try/except, ele vai ser executado mesmo ocorra algum erro ou não ocorra nenhum erro.
finally:
    print('FECHAR ARQUIVO')

# Try não pode ficar sozinha nem else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions