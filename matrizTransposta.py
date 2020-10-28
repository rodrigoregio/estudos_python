def matrizTransposta(minhaLista):
    i = 0
    j = 0
    linhas = len(minhaLista)
    colunas = len(minhaLista[0])
    print(f"A matriz possui {linhas} linhas e {colunas} colunas!")
    auxiliar = 0
    listaTransposta = []
    for i in range(colunas):
        listaTransposta.append([])
        print()
        for j in range(linhas):
            listaTransposta[i].append(minhaLista[j][i])
            print(listaTransposta[i][j], end='')

    return listaTransposta


teste = [[1, 2, 3], [4, 5, 6]   ]
print(teste)
testeTransposta = matrizTransposta(teste)
