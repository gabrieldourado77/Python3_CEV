
from time import sleep

t = 'Analisando o Triângulo v1.0'

print('='*50)
print('{:^50}'.format(t))
print('='*50)

r01 = float(input('Digite o comprimento da 1ª reta em cm: '))
r02 = float(input('Digite o comprimento da 2ª reta em cm: '))
r03 = float(input('Digite o comprimento da 3ª reta em cm: '))

print('='*50)
print('Verificando...')
sleep(0.5)

if r01 > r02 - r03 and r01 < r02 + r03:
    print('='*50)
    print('É possível formar um triângulo') 
elif r02 > r01 - r03 and r02 < r01 + r03:
    print('='*50)
    print('É possível formar um triângulo')
elif r03 > r01 - r02 and r03 < r01 + r02:
    print('='*50)
    print('É possível formar um triângulo')
else:
    print('='*50)
    print('Não é possível formar um triângulo')

print('='*65)
