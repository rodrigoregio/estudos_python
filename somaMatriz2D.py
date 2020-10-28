def soma2D(tabela1, tabela2):
    line = len(tabela1)
    column = len(tabela1)
    i = 0
    j = 0
    for i in range(line):
        for j in range(column):
            tabela1[i][j] += tabela2[i][j]

    return tabela1


t = [[5, 2, 8], [1, 4, 9], [6, 3, 7]]
s = [[2, 3, 4], [5, 6, 7], [8, 9, 0]]
print(soma2D(t, s))
