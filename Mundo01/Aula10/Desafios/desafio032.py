
from math import trunc

t = 'Desafio 32 - Ano Bissexto'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

a = trunc(float(input('Digite um ano: ')))

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é bissexto'.format(a))
else:
    print('O ano {} não é bissexto'.format(a))

print('='*65)
