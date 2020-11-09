# dados a serem ordenados:
# x=(25,57,48,37,12,92,86,33)
def mybubblesort(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def myinsertionsort(lista):
    for i in range(1, len(lista)):
        x = lista[i]
        j = i - 1
        while j >= 0 and x < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = x
    return lista


x = [25, 57, 48, 37, 12, 92, 86, 33]
print(f'Sem ordenação: {x}')
print(f'Com ordenação bolha: {mybubblesort(x)}')
x = [25,26,10,30,31,5,6,15]
print('Com ordenação por inserção: ', end='')
x = myinsertionsort(x)
print(x)
