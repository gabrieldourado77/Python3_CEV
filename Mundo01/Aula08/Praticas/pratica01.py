
from math import sqrt

t = 'Raiz Quadrada'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

n = int(input('Digite um número inteiro: '))
print('='*45)

raiz = sqrt(n)

print('A raiz quadrada de {} é {:.2f}'.format(n,raiz))
print('='*45)
