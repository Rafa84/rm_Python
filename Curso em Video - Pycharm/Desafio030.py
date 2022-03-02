p = int(input('Fale um numero, vou dizer se ele é par ou impar: '))
r = p %2
if r == 0:
    print('O número {} é um número PAR'.format(p))
else:
    print('O número {} é um número IMPAR'.format(p))
