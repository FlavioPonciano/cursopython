"""
CONSTANTE = "Variáveis" que não vão mudar, como no python não existe o conceito de constante há uma convenção de que constantes são todas as letras maiusculas na declaração.
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim) (quando mais blocos dentro blocos é ruim)
"""
# variável
velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

# constante
RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega
# Posso usar \ para quebrar linha e indicar ao python que o código segue

# Jogando as expressões dentro de variáveis podem auxiliar nos códigos
velocidade_carro_passou_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print('Velocidade ultrapassada.')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('Carro multado em radar 1')