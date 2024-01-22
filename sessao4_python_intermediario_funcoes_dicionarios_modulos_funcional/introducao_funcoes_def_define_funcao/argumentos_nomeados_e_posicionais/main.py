# Argumentos nomeados e não nomeados em funções Python
# Argumentos nomeados tem nome com sinal de igual
# Argumentos não nomeados recebem apenas o argumento (valor)


# Definilção | nome da função | (execução da função)
def soma(x, y, z):
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x+y+z)

soma(1, 2, 3) # Argumentos posicionais pois eles dependem da posição para sere recebidos pela função  
soma(y=2, z=3, x=1) # Argumentos nomeados, independe da ordem

soma(1, y=2, z=5) # Todos os paramêtros após primeiro nomeado precisam ser nomeados também.