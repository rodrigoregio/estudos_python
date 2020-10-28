# escreva a função palavras() que aceita uma string contendo o nome do arquivo e retorne a lista de palavras reais
# sem simbolos como ! @ , ,; ?
def palavras(arquivo):
    arquivoCompleto = open(arquivo, 'r')
    conteudo = arquivoCompleto.read()
    arquivoCompleto.close()

    letras = len(conteudo)
    tabela = str.maketrans('!@,.;?', 6 * ' ')
    conteudo = conteudo.translate(tabela)
    # print(f'O arquivo tem {0} letras e {1} palavras!'.format(letras, len(conteudo.split())))      encheção de linguiça
    return conteudo.split()


arq = 'D:/testePython.txt'
print(palavras(arq))
