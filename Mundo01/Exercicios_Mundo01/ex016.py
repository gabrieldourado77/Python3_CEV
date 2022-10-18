
from math import trunc

t = 'Quebrando um número'

print('='*35)
print('{:^35}'.format(t))
print('='*35)

n = float(input('Digite um número: '))

print('='*45)
print('A parte inteira de {} é {}'.format(n, trunc(n)))
print('='*45)

