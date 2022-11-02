
from math import trunc
from time import sleep

t = 'Exercício 67 - Tabuada v3.0'

print('='*50)
print('{:^50}'.format(t))
print('='*50)

num = 0
result = 0
c = 0

while True:

    num = trunc(float(input('Digite um número positivo: ')))
    print('='*50)

    if num > 0:
    
        for c in range(0,10):
            result = num * (c + 1)
            print(f'{num:^2} x {c + 1:^4} = {result:^4}')

        print('='*50)

    elif num == 0:
        print('O número não pode ser zero.')
        print('='*50)
    else:
        print('Finalizando...')
        sleep(1)
        break
    
print('='*60)
