# Implemente a função trocaPU() que aceita uma lista e teoca o primeiro e ultimo item da
# lista entao a lista [1,2,3] deve ficar [3,2,1].
def trocaPU(lista):
    tam = len(lista)
    lista[0], lista[len(lista) - 1] = lista[len(lista) - 1], lista[0]
    print(lista)


listinha = ['farinha', 'açucar', 'manteiga', 'maçãs']
print(listinha, end=' ')
print(' esta lista ficará ',end=' ')
trocaPU(listinha)
