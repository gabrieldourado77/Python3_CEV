
t = 'Desafio 23'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

n = int(input('Digite um número inteiro: '))

print('='*45)
print('Unidade: {}'.format(n // 1 % 10))
print('Dezena: {}'.format(n // 10 % 10))
print('Centena: {}'.format(n // 100 % 10))
print('Milhar: {}'.format(n // 1000 % 10))
print('='*45)
