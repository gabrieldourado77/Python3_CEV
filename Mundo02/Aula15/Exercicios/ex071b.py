
from math import trunc

t = 'Exercício 71 - Caixa Eletrônico'

print('='*50)
print('{:^50}'.format(t))

cedula200 = 0
cedula100 = 0
cedula50 = 0
cedula20 = 0
cedula10 = 0
cedula05 = 0
cedula02 = 0
moeda01 = 0


print('='*50)
val = trunc(float(input('Valor: R$ ')))

unidade = val // 1 % 10
dezena = val // 10 % 10
centena = val // 100 % 10
milhar = val // 1000 % 10


if unidade > 5:
    cedula05 += unidade // 5
    moeda01 = unidade % 5

elif unidade == 5:
    cedula05 += 1

elif unidade > 2:
    cedula02 += unidade // 2

    if unidade % 2 != 0:
        moeda01 = unidade % 2

elif unidade == 2:
    cedula02 += 1

elif unidade == 1:
    moeda01 += 1


if dezena >= 5:
    cedula50 += (dezena * 10) // 50

    if (dezena * 10) % 50 != 0:
        restoDezena = (dezena * 10) % 50
        cedula10 += restoDezena // 10

elif dezena >= 2:
    cedula20 += (dezena * 10) // 20
    
    if (dezena * 10) % 20 != 0:
        restoDezena = (dezena * 10) % 20
        cedula10 += restoDezena // 10

elif dezena == 1:
    cedula10 = 1


if centena == 1:
    cedula100 = 1
elif centena >= 2:
    cedula200 += (centena * 100) // 200

    if (centena * 100) % 200 != 0:
        restoCentena = (centena * 100) % 200
        cedula100 += restoCentena // 100


if milhar >= 1:
    cedula200 += (milhar * 1000) // 200


print('='*60)
print('Você receberá:')
print(f'{cedula200} cédula(s) de R$ 200')
print(f'{cedula100} cédula(s) de R$ 100')
print(f'{cedula50} cédula(s) de R$ 50')
print(f'{cedula20} cédula(s) de R$ 20')
print(f'{cedula10} cédula(s) de R$ 10')
print(f'{cedula05} cédula(s) de R$ 5')
print(f'{cedula02} cédula(s) de R$ 2')
print(f'{moeda01} moeda(s) de R$ 1')
print('='*60)
