
from math import trunc

t = 'Exercício 37 - Base de Conversão'

print('='*40)
print('{:^40}'.format(t))
print('='*40)

num = trunc(float(input('Digite um número: ')))
print('='*40)
print('Escolha a base de conversão: ')
print('Digite 1 para binário\nDigite 2 para octal\nDigite 3 para hexadecimal')
print('='*40)
esc = input('Escolha: ')

print('='*60)

if esc == '1':
    num = format(num,'b')
    print('Número em binário: {}'.format(num))
elif esc == '2':
    num = format(num,'o')
    print('Número em octal: {}'.format(num))
elif esc == '3':
    num = format(num,'x')
    print('Número em hexadecimal: {}'.format(num))
else:
    print('Opção inválida! Tente novamente.')

print('='*60)
