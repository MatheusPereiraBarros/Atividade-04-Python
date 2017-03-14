def calculaTempo(populacaoA, taxaA, populacaoB, taxaB):
    ano = 0
    while(populacaoA <= populacaoB):
        populacaoA = populacaoA * (1+(taxaA/100))
        ano += 1
    return ano

print(calculaTempo(50000, 3, 82500, 1.6))
