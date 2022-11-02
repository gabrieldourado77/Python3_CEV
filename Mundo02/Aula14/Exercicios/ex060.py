
from math import trunc, factorial

t = 'Exercício 60 - Cálculo do Fatorial'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

num = trunc(float(input('Digite um número: ')))
i = 0

print('='*60)

if num >= 0:

    if num == 0 or num == 1:
        print('{}! = 1'.format(num))
    
    else:
        i = num
        
        print('{}! = '.format(num), end='')

        # Coloquei, "enquanto i for maior do que 1, para que não apareça um X a mais do que o necessário."
        while i > 1:
            print('{} x '.format(i), end='')
            i = i - 1  

        fat = factorial(num)
        print('1 = {}'.format(fat))

else:
    print('O número não pode ser negativo!\nTente novamente.')

print('='*60)
