s = float(input('Digite o salario do colaborador: '))
if s > 1250:
    print('O aumento para esse salario é de 10%, portanto o novo salário é de {:.2f}'.format(s*1.1))
else:
    print('O aumento para esse salário é de 15%, portanto o novo salário é de {:.2f}'.format(s*1.15))
