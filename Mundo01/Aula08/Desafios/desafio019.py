
import random

e = 'Sorteando um item na lista'

print('='*45)
print('{:^45}'.format(e))
print('='*45)

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

escolha = random.choice([a1,a2,a3,a4])

print('='*45)
print('Aluno escolhido: {}'.format(escolha))
print('='*60)

