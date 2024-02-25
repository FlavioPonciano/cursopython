# Variaveis Livres (freevars) + nonlocal (locals, globals)
print(globals()) # mostra as variáveis globais
def fora(x):
    a = x # "a" é uma variável livre pois não está definida na função interna

    def dentro():
        print(locals()) # mostra quais são variáveis locais
        print(dentro.__code__.co_freevars) # ver as variáveis livres
        return a
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())

print('#' * 20)

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final # utilizo o nonlocal para informar ao python que a variavel interna não é local, então ele vai buscar fora da função interna essa variável.
        valor_final += valor_a_concatenar # então valor_final recebe o valor da string inicial e depois concatena os demais valores conforme desejado.
        return valor_final
    return interna

c = concatenar('a') # chamando a função externa para declarar um valor inicial
print(c('b')) # chamando a função interna que vai concatenar
print(c('c'))
print(c('d'))
final = c()
print(final)