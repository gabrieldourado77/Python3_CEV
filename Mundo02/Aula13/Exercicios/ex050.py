
from math import trunc
from sys import exit

t = ['Exercício 50', 'Soma dos Pares']

print('='*40)
print('{:^40}'.format(t[0]))
print('='*40)
print('{:^40}'.format(t[1]))
print('='*40)

s = 0
pares = 0

for c in range(0,6): 
    num = trunc(float(input('Digite o {}º número: '.format(c+1))))
    
    if num > 0:
        if num % 2 == 0:
            pares += 1
            s += num
    else:
        print('='*60)
        print('O número não pode ser zero, nem um valor negativo!\nTente novamente.')
        print('='*60)
        exit()

print('='*60)
print('Você digitou {} número(s) par(es)'.format(pares))
print('Resultado da Soma: {}'.format(s))
print('='*60)
