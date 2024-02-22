# Try, except, else e finally

# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    #print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido')
    # Como não sei qual erro ocorreu, posso utilizar "as" para indicar jogando em uma variável como classe:
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print("MSG:", error) # Primeiramente ele vai mostrar apenas a mensagem do erro
    print("Nome:", error.__class__.__name__) # Dentro da variável com class erro eu posso chamar a class e chamar o name 
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')