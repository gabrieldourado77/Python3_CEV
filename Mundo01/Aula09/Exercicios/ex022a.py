
t = 'Desafio 22'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

n01 = input('Digite o seu nome completo: ')
quant01 = len(''.join(n01.split()))
n02 = n01.split()

print('='*45)
print('Com letras maiúsculas: {}'.format(n01.upper()))
print('Com letras minúsculas: {}'.format(n01.lower()))
print('Quantidade de letras: {}'.format(quant01))
print('Quantidade de letras do primeiro nome: {}'.format(len(n02[0])))
print('='*45)
