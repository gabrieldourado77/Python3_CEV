
t = 'Desafio 26'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

f = input('Digite uma frase: ').strip().upper() 

print('='*45)
print('A letra "A" apareceu: {} vezes'.format(f.count('A')))
print('Posição da 1ª letra "A": {}º caracter'.format(f.find('A')+1))
print('Posição da última letra "A": {}º caracter'.format(f.rfind('A')+1))
print('='*65)
