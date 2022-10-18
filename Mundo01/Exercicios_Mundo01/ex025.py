
t = 'Desafio 25'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

n = input('Digite o seu nome: ').strip()

print('='*45)
print('Tem "Silva" no nome? {}'.format('SILVA' in n.upper().split()))
print('='*65)
