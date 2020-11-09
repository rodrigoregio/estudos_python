def busca_bin(lista, elementobuscado, indiceInicio, indiceFim):
    meio = (indiceInicio + indiceFim) // 2
    if elementobuscado == lista[meio]:
        return meio
    if elementobuscado < lista[meio]:
        busca_bin(lista, elementobuscado, 0, meio-1)
    if elementobuscado > lista[meio]:
        busca_bin(lista,elementobuscado,meio+1,indiceFim)
    return -1


minhalista = [8, 50, 740, 53, 48, 10, 69, 1, 9, 80]
minhalista.sort(minhalista)
pos1 = busca_bin(minhalista, 1)
