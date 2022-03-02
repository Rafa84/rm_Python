import math
x = float(input('Entre com o valor de um angulo: '))
print('O angulo informado é {}, seu seno é {:.2f}, o cosseno é: {:.2f} e a tangente é {:.2f}'.format(x, math.sin(math.radians(x)), math.cos(math.radians(x)), math.tan(math.radians(x))))