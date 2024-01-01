qtd_linhas = 5
qtd_colunas = 5

# O While interno vai rodar 5 vezes a cada loop do while externo (neste caso)

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1

print('Acabou')