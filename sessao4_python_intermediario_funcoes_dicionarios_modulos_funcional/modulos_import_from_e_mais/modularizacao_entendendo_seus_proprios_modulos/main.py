# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
try:
    import sys
    sys.path.append('/Users/Ponciano/Desktop') # Buscando localização de outros módulos e adicionando no path
except ModuleNotFoundError:
    ...

import modulo_python
# Importar um módulo de uma mesma pasta
import importado_modulo
print('Esse módulo se chama', __name__)
print(*sys.path, sep='\n') # Mostrando as pastas e os caminhos que contém módulos ou podem vir a conter.

# Interessante é criar os módulos na mesma pasta do arquivo main e criar o arquivo em volta desse main e criar os pacotes "pastas" abaixo dele