x = int(input('Por favor, me informe a sua velocidade: '))
m = (x - 80)*7
if x < 80:
    print('Muito bem, continue sua viagem em segurança')
else:
    print('Velocidade acima da permitida. Uma multa no valor de {} reais foi encaminhada ao seu endereço'.format(m))

