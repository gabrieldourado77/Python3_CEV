
from math import trunc

t = 'Exercício 37 - Base de Conversão'

print('='*40)
print('{:^40}'.format(t))
print('='*40)

num = trunc(float(input('Digite um número: ')))
print('='*40)
print('Escolha a base de conversão: ')
print('[1] Binário\n[2] Octal\n[3] Hexadecimal')
print('='*40)
opcao = input('Opção: ')

print('='*60)

if opcao == '1':
    print('Número em binário: {}'.format(bin(num) [2:]))
elif opcao == '2':
    print('Número em octal: {}'.format(oct(num) [2:]))
elif opcao == '3':
    print('Número em hexadecimal: {}'.format(hex(num) [2:]))
else:
    print('Opção inválida! Tente novamente.')

print('='*60)
