
from math import sqrt

t = 'Catetos e Hipotenusa'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))

h = sqrt(pow(co,2) + pow(ca,2))

print('='*45)
print('Hipotenusa: {:.2f}cm'.format(h))
print('='*45)
