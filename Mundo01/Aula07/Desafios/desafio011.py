
t = 'Pintando uma parede'

print('='*50)
print('{:^50}'.format(t))
print('='*50)

alt = float(input('Digite a altura da parede em metros: '))
print('='*50)
larg = float(input('Digite a largura da parede em metros: '))
print('='*50)

area = alt*larg
tinta = area/2

print('Área da parede: {:.2f} m²'.format(area))
print('Quantidade de tinta necessária: {:.2f} litros'.format(tinta))
print('='*50)

