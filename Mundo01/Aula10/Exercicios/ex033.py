
from math import trunc

t = 'Desafio 33 -  Maior e Menor'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

n01 = trunc(float(input('Digite o 1º número: ')))
n02 = trunc(float(input('Digite o 2º número: ')))
n03 = trunc(float(input('Digite o 3º número: ')))

if n01 > n02 and n01 > n03:
    print('='*45)
    print('O número maior é o {}'.format(n01))
elif n02 > n01 and n02 > n03:
    print('='*45)
    print('O número maior é o {}'.format(n02))
else:
    print('='*45)
    print('O número maior é o {}'.format(n03))

if n01 < n02 and n01 < n03:
    print('O número menor é o {}'.format(n01))
elif n02 < n01 and n02 < n03:
    print('O número menor é o {}'.format(n02))
else:
    print('O número menor é o {}'.format(n03))

print('='*65)

