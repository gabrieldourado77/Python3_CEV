
from math import sin, cos, tan

e = 'Seno, Cosseno e Tangente'

print('='*45)
print('{:^45}'.format(e))
print('='*45)

ang = float(input('Digite o valor do ângulo: '))

s = sin(ang)
c = cos(ang)
t = tan(ang)

print('='*45)
print('Seno: {:.3f}\nCosseno: {:.3f}'.format(s,c))
print('Tangente: {:.3f}'.format(t))
print('='*45)
