
t = 'Calculando descontos'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

p = float(input('Digite o preço do produto: R$ '))
np = p - (p*(5/100))

print('='*45)
print('Desconto: 5%')
print('Preço com desconto: R$ {:.2f}'.format(np))
print('='*45)
