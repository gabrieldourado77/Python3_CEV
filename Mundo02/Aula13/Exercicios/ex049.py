
from math import trunc

t = ['Exercício 49', 'Tabuada v2.0']

print('='*40)
print('{:^40}'.format(t[0]))
print('='*40)

n = trunc(float(input('Digite um número inteiro: ')))

if n > 0:
    print('='*40)
    print('{:^40}'.format(t[1]))
    print('='*40)

    for i in range(0,10):
        cont = i + 1
        mult = n * cont
        print('{:^2} X {:^2} = {:^2}'.format(n, cont, mult))

else:
    print('='*60)
    print('O número não pode ser zero, nem negativo! Tente novamente.')

print('='*60)    
