# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

# groupby precisa que ordene a lista para funcionar
# Ordenando a lista:
alunos_agrupados = sorted(alunos, key=ordena) # utilizando uma função como key para que não seja repetido todo o valor em mais de um caso, mas de toda forma posso utilizar a função lambda

# utilizando a função lambda para informar a key que será utiliza para separar os grupos
grupos = groupby(alunos_agrupados, key=ordena)

# Fazendo um for para mostrar melhor os grupos
for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)