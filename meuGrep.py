def meu_grep(arquivo, substring):
    arqEntrada = open(arquivo, 'r')
    listaLinhas = arqEntrada.readlines()
    arqEntrada.close()

    for linha in listaLinhas:
        if substring in linha:
            print(linha)


caminhoArq = input("Insira o nome do arquivo com o caminho:")
string = input('Insira uma palavra para procurar no arquivo: ')
meu_grep(caminhoArq, string)
