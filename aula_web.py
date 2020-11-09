from urllib.request import urlopen


def pegaFonte(url, topicos):
    resposta = urlopen(url)
    html = resposta.read()
    html = html.decode()
    indice = 0
    while indice < len(topicos):
        print(f'A palavra {topicos[indice]} aparece {html.count(topicos[indice])}.')
        indice = indice + 1
        #print(indice)
