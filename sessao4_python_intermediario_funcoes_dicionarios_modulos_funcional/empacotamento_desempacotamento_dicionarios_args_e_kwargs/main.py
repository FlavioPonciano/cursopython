# Empacotamento e desempacotamento de dicionários + *args e **kwargs

# desempacotando e empacotamento comum
a, b = 1, 2
a, b = b, a
#print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

a, b = pessoa
print(a, b) # retorna apenas as chaves

a, b = pessoa.values()
print(a, b) # retorna apenas os valores
a, b = pessoa.items()
print(a, b) # retorna tuplas contendo chave e valor respectivamente

print("#" * 20)

# esse é o mesmo que realizar um for
(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

print("#" * 20)

for chave, valor in pessoa.items():
    print(chave, valor)

print("#" * 20)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6
}

# Posso extair um dicionário para outro podendo extair quantos eu quiser, isso é um desempacotamento:
pessoa_completa = {**pessoa, **dados_pessoa, 'chave': "adicionei mais uma chave"} # posso adicionar e alterar chaves e valores

print(pessoa_completa)

print("#" * 20)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

#argumentos não nomeados como 1 e 2 não vão cair no kwargs e sim no args
mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)

# Posso desempacotar um dicionário
mostro_argumentos_nomeados(**pessoa_completa)