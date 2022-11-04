
from math import trunc

t = 'Exercício 71 - Caixa Eletrônico'

quantCedulas = 0
cedula = 200
quantMoedas = 0
moeda01 = 1

print('='*50)
print('{:^50}'.format(t))
print('='*50)

valor = trunc(float(input('Valor: R$ ')))
total = valor

print('='*60)
print('Você receberá:')

while True:

    if total >= cedula:
        total = total - cedula
        quantCedulas += 1
    else:
        if quantCedulas > 0:
            print(f'{quantCedulas} cédula(s) de R$ {cedula}')

        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            
            while total >= moeda01:
                total = total - moeda01
                quantMoedas += 1
        
            if quantMoedas > 0:
                print(f'{quantMoedas} moeda(s) de R$ 1')

        quantCedulas = 0
        quantMoedas = 0

        if total == 0:
            break

print('='*60)
