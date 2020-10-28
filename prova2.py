def amortizada(notas):
    i = 0
    CONST_x = 4
    h = (3 / ((1 / (notas[0] + CONST_x)) + (1 / (notas[1] + CONST_x)) + (1 / (notas[2] + CONST_x)))) - CONST_x
    if h >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado')
    return h


meuI = 0
minhas_notas = [0, 0, 0]
for meuI in range(0, 3):
    minhas_notas[meuI] = int(input(f'Insira a nota {meuI+1} '))
print(amortizada(minhas_notas))
