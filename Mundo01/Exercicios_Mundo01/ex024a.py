
t = 'Desafio 24'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

c = input('Digite o nome da cidade: ').split()

print('='*45)
print('Começa com "Santo"? {}'.format('Santo' in c[0]))
print('='*65)
