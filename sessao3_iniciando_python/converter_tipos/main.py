# Conversão de tipos, coerção, type convertion, typecasting, coercion: é o ato de converter um tipo de dado em outro tipo, imutáveis e primitivoos.
# str, int, float, bool

print(1 + 1) #somar
print("a" + "b") #concatenar

print("1", type("1")) # Mostrando o type string
print(int("1"), type(int("1"))) # Fazendo a coerção do tipo para inteiro (int)
print(int('1') + int('1')) # Convertando dois inteiros para soma

#Float - vai ter um resultado do tipo float mesmo somando com int
print(float('1') + 1)

#Bool - de acordo com cada conteúdo o bool vai ter um retorno diferente, como uma string vazia tem valor de false e outra com espaço tem valor de true.
print(bool(''), bool(' '))

#String - convertendo para string
print(str(11) + 'b')