
from math import trunc

t = 'Exercício 38 - Comparando Números'

print('='*40)
print('{:^40}'.format(t))
print('='*40)

n01 = trunc(float(input('Digite o 1º número: ')))
n02 = trunc(float(input('Digite o 2º número: ')))

print('='*40)

if n01 > n02:
    print('O primeiro valor é o maior')
elif n02 > n01:
    print('o segundo valor é o maior')
else:
    print('Os dois valores são iguais')
    
print('='*55)
