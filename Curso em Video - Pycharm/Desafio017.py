import math
x1 = float(input('Entre com o valor do Cateto oposto: '))
x2 = float(input('Entre com o valor do Cateto adjacente: '))
h = math.hypot(x1,x2)
print('O valor da hipotenusa é: {:.2f}'.format(h))