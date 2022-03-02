import random
a = str(input('Digite o primeiro nome: '))
b = str(input('Digite o segundo nome: '))
c = str(input('Digite o terceiro nome: '))
d = str(input('Digite o quarto nome: '))
alunos = [a, b, c, d]
random.shuffle(alunos)
print('A ordem de apresentação será: ')
print(alunos)