
from math import trunc

t = 'Exercício 52 - Números Primos'

print('='*40)
print('{:^40}'.format(t))
print('='*40)

n = trunc(float(input('Digite um número inteiro: ')))
divisivel = 0

if n > 1:

    for c in range(1, n+1):
        if n % c == 0:
            divisivel += 1

    print('='*60)
    print('O número {} '.format(n),end='')

    if divisivel == 2:
        print('é primo.')
    else:
        print('não é primo.')

else:
    print('='*60)
    print('O número deve ser maior do que 1! Tente novamente.')

print('='*60)
