from random import randint
x = int(input('Escolhi um número entre 0 e 5, tente adivinhar: '))
y = randint(0,5)
if x == y:
    print('Parabens, voce adivinhou meu numero')
else:
    print('Que pena, eu pensei no numero {} e nao em {}'.format(y,x))

