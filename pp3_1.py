'Implemente um programa que solicita a temperatura atual em graus Fahrenheit e exibe a mesma em graus Celsius usando a fórmula Celsius = 5/9*(fahrenheit-32)'
fah = float(input('Informe a temperatura em graus Fahrenheit:\n'))
celsius = 5/9*(fah-32)
print('Temperatura digitada em Fahrenheit: '+str(fah)+'\nTemperatura em graus celsius = '+str(celsius)+'')
