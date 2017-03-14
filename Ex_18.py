def imprimirTabuada(inicio, final):
    for i in range(inicio, final+1):
        for j in range(1, 11):
            print("%6.2f x %6.2f = %8.2f" %(i, j, i*j))

imprimirTabuada(5,8)
