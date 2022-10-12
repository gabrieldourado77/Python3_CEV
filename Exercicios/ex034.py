
from time import sleep

t = 'Desafio 34 - Aumento Salarial'

print('='*50)
print('{:^50}'.format(t))
print('='*50)

s = float(input('Digite o salário do funcionário: R$ '))

print('='*45)
print('Calculando...')
sleep(1)

if s > 1250:
    s = s + s*(10/100) 
    print('='*45)
    print('Aumento Salarial: 10%')
    print('Salário com aumento: R$ {:.2f}'.format(s))
elif s > 0:
    s = s + s*(15/100)
    print('='*45)
    print('Aumento Salarial: 15%')
    print('Salário com aumento: R$ {:.2f}'.format(s))
else:
    print('='*65)
    print('Você digitou um valor negativo. Tente novamente!')

print('='*65)
