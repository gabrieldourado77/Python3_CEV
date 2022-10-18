
import random

e = 'Sorteando uma ordem na lista'

print('='*45)
print('{:^45}'.format(e))
print('='*45)

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

ordem = random.sample([a1,a2,a3,a4],k=4)

print('='*70)
print('Ordem de Apresentação: {}'.format(ordem))
print('='*70)
