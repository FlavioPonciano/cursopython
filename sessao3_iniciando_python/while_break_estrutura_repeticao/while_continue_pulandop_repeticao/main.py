contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6')
        continue

    # Pulando algumas linhas do resultado.
    if contador >= 10 and contador <= 27:
        # Se fosse adicionado um print aqui ele iria mostrar.
        continue

    # A posição do contador ou do print interfere no resultado.    
    print(contador)

    if contador == 40:
        break

print('Acabou')


