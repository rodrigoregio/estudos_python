def temQuatroLetras(lista):
    for item in lista:
        if len(item) == 4:
            print(item, sep=' ', end=' ')

lista=[]
item=input("Informe a palavra: ")
while item != "":
    lista.append(item)
    item = input("Informe a palavra: ")
lista.sort()
temQuatroLetras(lista)