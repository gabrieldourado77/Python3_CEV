
from math import hypot, sin, cos, tan

e = 'Resoluções Diferentes dos Desafios'

print('='*45)
print('{:^45}'.format(e))
print('='*45)

n = 10.90
hip = hypot(15,25)
ang = 45
s = sin(ang)
c = cos(ang)
t = tan(ang)


print('A parte inteira de {} é {}'.format(n,int(n)))
print('='*45)
print('Hipotenusa: {:.2f}'.format(hip))
print('='*45)
print('Seno: {:.3f}\nCosseno: {:.3f}\nTangente: {:.3f}'.format(s,c,t))
print('='*45)

