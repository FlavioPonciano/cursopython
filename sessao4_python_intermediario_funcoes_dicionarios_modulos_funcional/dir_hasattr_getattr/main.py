# dir, hasattr e getattr em Python
string = 'Flávio'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)

# dir posso utilizar no debugger console para ver todos os atributos daquele tipo de objeto

# hasattr vai ercontrar o atributo dentro da lista daquele tipo de objeto
    
# getattr vai chamar o atributo para ser utilizado