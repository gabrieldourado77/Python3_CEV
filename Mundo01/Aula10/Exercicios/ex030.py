
from math import trunc

t = 'Desafio 30 - Par ou Ímpar'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

n = trunc(float(input('Digite um número inteiro: ')))

if n % 2 == 0:
    print('='*45)
    print('O número {} é par'.format(n))
else:
    print('O número {} é ímpar'.format(n))

print("="*65)
