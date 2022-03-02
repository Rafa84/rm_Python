import random
num = random.randint(0,9999)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000
print('Analise do numero {}'.format(num))
print('O numero tem {} unidade(s)'.format(u))
print('O numero tem {} dezena(s)'.format(d))
print('O numero tem {} centena(s)'.format(c))
print('O numero tem {} milhare(s)'.format(m))