
t = 'Desafio 24'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

c = input('Digite o nome da cidade: ').strip()

print('='*45)
print('Começa com "Santo"? {}'.format(c[:5].upper() == 'SANTO'))
print('='*65)
