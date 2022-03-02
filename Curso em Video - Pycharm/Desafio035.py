r1 = float(input('Informe o primeiro comprimento de reta: '))
r2 = float(input('Informe o segundo comprimento de reta: '))
r3 = float(input('Informe o terceiro comprimento de reta: '))
if r1 < r2 + r3 and r2 <  r3 + r1 and r3 < r1 + r2:
    print('Os três segmentos formam um triangulo.')
else:
    print('Os segmentos não formam um triangulo.')