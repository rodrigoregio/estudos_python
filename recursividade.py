from turtle import *
import os
from time import sleep


def vertical(numero):  # feito com o autor
    if numero < 10:
        print(numero)
    else:
        print(numero % 10)
        vertical(numero // 10)


def vertical_inverso(numero):  # problema prático 10.1
    if numero < 10:
        print(numero)
    else:
        vertical_inverso(numero // 10)
        print(numero % 10)


def cheers(numero):  # problema prático 10.2
    if numero <= 0:
        print('Hurrah')
    else:
        print('Hip, ', end='')
        cheers(numero - 1)


def padrao_numerico(numero):
    if numero <= 0:
        print(0, end=' ')
    else:
        padrao_numerico(numero - 1)
        print(numero, end=' ')
        padrao_numerico(numero - 1)


def padrao_asterisk(numero):  # problema prático 10.4
    if numero <= 1:
        print('*')
    else:
        padrao_asterisk(numero - 1)
        print('*' * numero)
        padrao_asterisk(numero - 1)


def koch(numero):
    if numero == 0:
        return 'F'
    temp = koch(numero - 1)
    return temp + 'L' + temp + 'R' + temp + 'L' + temp


def drawKoch(n):
    s = Screen()
    t = Turtle()
    directions = koch(n)
    for move in directions:
        if move == 'F':
            print('F')
            t.forward(300 / 3 ** n)
        if move == 'L':
            print('L')
            t.lt(60)
        if move == 'R':
            print('R')
            t.rt(120)
    s.bye()


def scan(pathname, signatures):
    """ varre recursivamente os arquivos contidos direta ou indiretamente na pasta pathname """
    for item in os.listdir(pathname):
        proximo = os.path.join(pathname, item)
        try:
            scan(proximo, signatures)
        except:
            for confidencial in signatures:
                if open(proximo).read().find(signatures[confidencial]) >= 0:
                    print('{}, pode conter dados confidenciais {}'.format(proximo, confidencial))


class Ponto:
    x = 0
    y = 0
