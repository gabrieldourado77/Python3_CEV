
t = 'Catetos e Hipotenusa'

print('='*45)
print('{:^45}'.format(t))
print('='*45)

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))

hip = (co**2 + ca**2)**(1/2)

print('='*45)
print('Hipotenusa: {:.2f}cm'.format(hip))
print('='*45)
