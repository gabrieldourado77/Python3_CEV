
from time import sleep

t = 'Exercício 42 - Analisando Triângulos v2.0'

print('='*50)
print('{:^50}'.format(t))
print('='*50)

r01 = float(input('Comprimento da 1ª reta em cm: '))
r02 = float(input('Comprimento da 2ª reta em cm: '))
r03 = float(input('Comprimento da 3ª reta em cm: '))

print('='*50)
print('Verificando...')
sleep(0.5)

print('='*65)

if r01 < r02 + r03 and r02 < r01 + r03 and r03 < r01 + r02:
    print('É possível formar um triângulo', end=' ')
    
    if r01 == r02 and r01 == r03: 
        print('equilátero.')
    elif r01 != r02 and r01 != r03 and r02 != r03:
        print('escaleno.')
    else:
        print('isósceles.')

else:
    print('Não é possível formar um triângulo')

print('='*65)

