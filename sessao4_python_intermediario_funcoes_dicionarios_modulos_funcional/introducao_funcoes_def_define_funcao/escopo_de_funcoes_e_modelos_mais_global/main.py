"""
Escopo de funções em Python
Escopo significa o loca onde aquele código pode atingir
Existe o escopo global e o local
O escopo global é o escopo onde todo o código é alcançavel
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados
Não temos acesso a nomes de escopos internos nos escopos externos
A palavra global faz uma variável do escopo extgerno ser a mesma do escopo interno.
"""

x = 1


def escopo():
    x = 10

    def outra_funcao():
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)

