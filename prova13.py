def amortizada(notas):
    i = 0
    h=0
    for i in range(len(notas)):
        h = 3 / (1 / (notas[i] + 4)) - 4
    return h


meuI = 0
notas = [0, 0, 0]
for meuI in range(0, 2):
    notas[meuI] = int(input())
print(amortizada(notas))
