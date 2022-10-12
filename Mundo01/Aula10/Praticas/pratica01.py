
from math import trunc
from datetime import date

t = 'O Ano Atual é Bissexto?'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

a = trunc(float(input('Digite 0 para analisar o ano atual: ')))

if a == 0:
    a = date.today().year

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano de {} é bissexto'.format(a))
else:
    print('O ano de {} não é bissexto'.format(a))

print('='*65)
