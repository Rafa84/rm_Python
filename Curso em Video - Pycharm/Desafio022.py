nome = str(input('Digite seu nome completo: ')).strip()
print('O seu nome em letras maiusculas é {}'.format(nome.upper()))
print('O seu nome em letras minuscula é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
# outra forma de fazer a ultima etapa!
separa = nome.split()
print('O seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))