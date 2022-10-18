
t = 'Desafio 31 - Custo da Viagem'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

d = float(input('Distância da viagem em Km: '))

if d > 0 and d<=200:
    p = d * 0.50
    print('='*45)
    print('Preço da Passagem: R$ {:.2f}'.format(p))
else:
    p = d * 0.45
    print('='*45)
    print('Preço da Passagem: R$ {:.2f}'.format(p))

print('='*65)
