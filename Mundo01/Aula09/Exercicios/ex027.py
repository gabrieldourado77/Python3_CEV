
t = 'Desafio 27'

print('='*45)
print('{:^45}'.format(t))
print('='*60)

n = input('Digite o seu nome completo: ').strip()
completo = n.title().split()
ultimo  = len(completo) - 1

print('='*60)
print('Primeiro nome: {}'.format(completo[0]))
print('Último nome: {}'.format(completo[ultimo]))
print('='*65)
