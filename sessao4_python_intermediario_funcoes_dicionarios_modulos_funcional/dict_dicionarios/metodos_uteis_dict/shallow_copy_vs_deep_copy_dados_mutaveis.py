# Shallow Copy vs Deep Copy
#copy - retorna uma cópia rasa (shallow copy)

# Para fazer deep copy eu preciso importar um módulo do Python
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

# d2 aponta para o mesmo local da memória de d1
d2 = d1
d2['c1'] = 1000
print(d1)

# Shallow copy (cópia rasa)
# Agora se eu uso o copy ele vai pegar o valor e copiar gerando um novo endereço de memória para itens imutaveis, para itens mutaveis ambos vão apontar para o mesmo lugar na memória.
d3 = d2.copy()
d3['c1'] = 50
d3['l1'][1] = 9999 # todas as listas recebem essa alteração


print(d1)
print(d2)
print(d3)

print('#' * 10)

# Utilizando a deep copy
d4 = copy.deepcopy(d1)
d4['l1'][1] = 8888 # onde todos os valores inclusive os mutaveis serão alterados somente dentro desse dicionário.


print(d1)
print(d2)
print(d3)
print(d4)
