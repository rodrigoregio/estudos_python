def ponto_em_virgula(numero):
    num = str(numero);
    if "," in num:
        indexOfVirgula= num.find(",");
        num=num.replace(',', '.')
        print(num);

numero=input("Insira um numero com virgula");
ponto_em_virgula(numero);