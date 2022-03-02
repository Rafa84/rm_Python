n = int(input("Quantos dias o carro foi alugado: "))
n1 = float(input('Quantos Km foram rodados nesses dias: '))
print('O carro foi alugado por {} dias e rodou {}km, o valor a ser pago pelo aluguel é de {:.2f} reais.'.format(n, n1, ((n*60)+(n1*0.15))))