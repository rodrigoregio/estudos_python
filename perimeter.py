from math import pi


def perimeter(raio):
    'retorna perimetro de um circulo pelo raio informado'
    return 2 * pi * raio


def negatives(lista):
    'imprime em tela os numeros negativos'
    for item in lista:
        if item < 0:
            print(item)

def teste_encapsulamento(a,b,c):
    'testando encapsulamento de parametros'
    print('primeiro parametro: {}'.format(a))
    print('segundo parametro: {}'.format(b))
    print('terceiro parametro: {}'.format(a))
    print('Valor de A: {}'.format(a))
    print(x)

x=5
y=7
z=9
teste_encapsulamento(x, y, z)
print(x)