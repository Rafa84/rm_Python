d = float(input('Olá, vamos calcular a sua viagem! Por favor, me diga a distancia, em KM, viajada: '))
if d<200:
    print('O valor da passagem ficou em {} reais'.format(d*0.5))
else:
    print('O valor da passagem ficou em {} reais'.format(d*0.45))

