
t = 'Desafio 22'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

n = input('Digite o seu nome completo: ')

print('='*45)
print('Quantidade de letras: {}'.format(len(n) - n.count(' ')))
print('Quantidade de letras do primeiro nome: {}'.format(n.find(' ')))
print('='*45)
