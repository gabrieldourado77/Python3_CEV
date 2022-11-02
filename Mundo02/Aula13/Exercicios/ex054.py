
from math import trunc
from datetime import date

t = 'Exercício 54 - Maioridade'

print('='*40)
print('{:^40}'.format(t))
print('='*50)

atual = date.today().year
maiores = 0
menores = 0

for c in range(0,7):
    nasc = trunc(float(input('Ano de Nascimento da {}ª pessoa: '.format(c+1))))

    if atual - nasc >= 21:
        maiores += 1 
    else:
        menores += 1

print('='*60)
print('Quant. de pessoas maiores de idade: {}'.format(maiores))
print('Quant. de pessoas menores de idade: {}'.format(menores))
print('='*60)
