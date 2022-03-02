nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split()
print('Seu primeiro nome é: {}'.format(separado[0].capitalize()))
print('Seu ultimo nome é: {}'.format(separado[-1].capitalize()))