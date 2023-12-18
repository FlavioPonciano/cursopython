a = 'A'
b = 'B'
c = 1.1

string = 'a={0} b={1} c={nome3:.2f} d={0}' #posso colocar essas '' direto na variável abaixo

formato = string.format(a, b, nome3=c) #o format leva em consideração a sequencia entre parenteses, mas podemos utilizar os indices de cada item para mostrar
#nome3 é um parametro os demais sem nome são argumentos e caso nomeie um parametro o que vem após também precisa ser nomeado

#parametro nomeado é quando dou nome para os itens dentro das chamadas ou criação das funções

print(formato)