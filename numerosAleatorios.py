from random import randint


def gerar(num):
    i = 0
    lista = []
    while i <= num:
        numero_aleatorio = randint(10, 50)
        if numero_aleatorio not in lista:
            lista.append(numero_aleatorio)
            i += 1
        else:
            i -= 1

    return lista


numero = input('Informe quantidade de numeros aleatorios: ')
numero = int(numero)
globalLista = gerar(numero)
print('Lista gerada:', globalLista)
