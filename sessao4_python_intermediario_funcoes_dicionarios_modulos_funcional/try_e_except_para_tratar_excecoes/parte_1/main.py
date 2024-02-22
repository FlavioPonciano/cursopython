# Try, except, else e finally
# Erros não devem ser sileciados

# Erros criam execeções e encerram laços e não tratar o erro da forma correta pode acarretar que outros erros fiquem escondidos.

# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
    # Forma certa de tratar o erro é identificar o mesmo e passar o nome no except:
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido')
    # Posso tratar mais de uma erro em uma linha só, porém não se sabe qual exeção ocorreu:
except (TypeError, IndexError):
    print('TypeError + IndexError')
    # Exception é o mais nível entre as execeções e ele vai pegar qualquer erro que aconteça:
except Exception: # É o ultimo nível de tratamento do erro e deve ser usado em ultimo caso, pois pode dificultar o trabalho de encontrar o erro especifico e solucionar ou indicar ao usuário o problema.
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')