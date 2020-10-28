# O desafio desta semana é pensar em como processar um determinado conjunto de valores de entrada e gerar como saída um
# resultado esperado. Por exemplo, se quisermos calcular a média de notas de provas de um aluno, precisamos passar para
# o programa as notas dessas provas e, dentro do programa, realizar a soma dessas notas, para dividir pela quantidade.
# Tais operações são realizadas por expressões aritméticas e operadores que serão vistos nesta semana.
# Vamos um pouco além para pensar que podemos encontrar outros desafios dentro da nossa primeira situação problema: e se
# o valor da nota for um número negativo? E se for um valor não numérico? E se quisermos armazenar também o nome do
# aluno?
from time import sleep
def is_number(valor):
    teste = 0
    try:
        teste = float(valor)
    except ValueError:
        return teste-1
    return teste

nota = 0
soma = 0
contador = 0
continua = True
nome = input('Informe seu nome: ')
while continua:
    nota = is_number(input('Informe sua nota: '))
    if nota <= 0:
        print('Nota invalida, informe valor maior ou igual a 0.')
    else:
        soma += nota
        contador += 1
    c = str(input('Deseja continuar? Informe \'s\' ou \'n\''))
    if c == 's':
        continua = True
    elif c == 'n':
        continua = False
    else:
        print('Valor inválido, o programa irá continuar.')
        continua = True
media = soma/contador
print('-='*20)
print('Dados do aluno:\nNome do aluno: '+nome+'\nMedia: '+str(media))
sleep(3)
